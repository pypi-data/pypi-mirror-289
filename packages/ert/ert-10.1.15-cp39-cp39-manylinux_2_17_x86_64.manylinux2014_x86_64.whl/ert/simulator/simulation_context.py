from __future__ import annotations

import asyncio
import contextlib
from threading import Thread
from time import sleep
from typing import TYPE_CHECKING, Any, List, Optional, Tuple, Union

import numpy as np

from _ert.threading import ErtThread
from ert.config import HookRuntime
from ert.enkf_main import create_run_path
from ert.ensemble_evaluator import Realization
from ert.job_queue import JobQueue, JobStatus
from ert.run_context import RunContext
from ert.runpaths import Runpaths
from ert.scheduler import Scheduler, create_driver
from ert.scheduler.job import State as JobState
from ert.shared.feature_toggling import FeatureScheduler

from .forward_model_status import ForwardModelStatus

if TYPE_CHECKING:
    import numpy.typing as npt

    from ert.enkf_main import EnKFMain
    from ert.run_arg import RunArg
    from ert.storage import Ensemble


def _slug(entity: str) -> str:
    entity = " ".join(str(entity).split())
    return "".join([x if x.isalnum() else "_" for x in entity.strip()])


def _run_forward_model(
    ert: "EnKFMain",
    job_queue: Union["JobQueue", "Scheduler"],
    run_context: "RunContext",
) -> None:
    # run simplestep
    asyncio.run(_submit_and_run_jobqueue(ert, job_queue, run_context))


async def _submit_and_run_jobqueue(
    ert: "EnKFMain",
    job_queue: Union["JobQueue", "Scheduler"],
    run_context: "RunContext",
) -> None:
    max_runtime: Optional[int] = ert.ert_config.analysis_config.max_runtime
    if max_runtime == 0:
        max_runtime = None
    for index, run_arg in enumerate(run_context):
        if not run_context.is_active(index):
            continue
        if isinstance(job_queue, JobQueue):
            job_queue.add_job_from_run_arg(
                run_arg,
                ert.ert_config.queue_config.job_script,
                max_runtime,
                ert.ert_config.preferred_num_cpu,
            )
        else:
            realization = Realization(
                iens=run_arg.iens,
                forward_models=[],
                active=True,
                max_runtime=max_runtime,
                run_arg=run_arg,
                num_cpu=ert.ert_config.preferred_num_cpu,
                job_script=ert.ert_config.queue_config.job_script,
            )
            job_queue.set_realization(realization)

    required_realizations = 0
    if ert.ert_config.analysis_config.stop_long_running:
        required_realizations = (
            ert.ert_config.analysis_config.minimum_required_realizations
        )
    with contextlib.suppress(asyncio.CancelledError):
        await job_queue.execute(required_realizations)


class SimulationContext:
    def __init__(
        self,
        ert: "EnKFMain",
        ensemble: Ensemble,
        mask: npt.NDArray[np.bool_],
        itr: int,
        case_data: List[Tuple[Any, Any]],
    ):
        self._ert = ert
        self._mask = mask

        if FeatureScheduler.is_enabled(ert.ert_config.queue_config.queue_system):
            driver = create_driver(ert.ert_config.queue_config)
            self._job_queue = Scheduler(
                driver, max_running=ert.ert_config.queue_config.max_running
            )
        else:
            self._job_queue = JobQueue(ert.ert_config.queue_config)
        # fill in the missing geo_id data
        global_substitutions = ert.ert_config.substitution_list
        global_substitutions["<CASE_NAME>"] = _slug(ensemble.name)
        for sim_id, (geo_id, _) in enumerate(case_data):
            if mask[sim_id]:
                global_substitutions[f"<GEO_ID_{sim_id}_{itr}>"] = str(geo_id)
        self._run_context = RunContext(
            ensemble=ensemble,
            runpaths=Runpaths(
                jobname_format=ert.ert_config.model_config.jobname_format_string,
                runpath_format=ert.ert_config.model_config.runpath_format_string,
                filename=str(ert.ert_config.runpath_file),
                substitution_list=global_substitutions,
            ),
            initial_mask=mask,
            iteration=itr,
        )

        create_run_path(self._run_context, self._ert.ert_config)
        self._ert.runWorkflows(
            HookRuntime.PRE_SIMULATION, None, self._run_context.ensemble
        )
        self._sim_thread = self._run_simulations_simple_step()

        # Wait until the queue is active before we finish the creation
        # to ensure sane job status while running
        while self.isRunning() and not self._job_queue.is_active():
            sleep(0.1)

    def get_run_args(self, iens: int) -> "RunArg":
        """
        raises an exception if no iens simulation found

        :param iens: realization number
        :return: run_args for the realization
        """
        for run_arg in iter(self._run_context):
            if run_arg is not None and run_arg.iens == iens:
                return run_arg
        raise KeyError(f"No such realization: {iens}")

    def _run_simulations_simple_step(self) -> Thread:
        sim_thread = ErtThread(
            target=lambda: _run_forward_model(
                self._ert, self._job_queue, self._run_context
            )
        )
        sim_thread.start()
        return sim_thread

    def __len__(self) -> int:
        return len(self._mask)

    def isRunning(self) -> bool:
        # TODO: Should separate between running jobs and having loaded all data
        return self._sim_thread.is_alive() or self._job_queue.is_active()

    def getNumPending(self) -> int:
        if isinstance(self._job_queue, JobQueue):
            return self._job_queue.count_status(JobStatus.PENDING)  # type: ignore
        return self._job_queue.count_states()[JobState.PENDING]

    def getNumRunning(self) -> int:
        if isinstance(self._job_queue, JobQueue):
            return self._job_queue.count_status(JobStatus.RUNNING)  # type: ignore
        return self._job_queue.count_states()[JobState.RUNNING]

    def getNumSuccess(self) -> int:
        if isinstance(self._job_queue, JobQueue):
            return self._job_queue.count_status(JobStatus.SUCCESS)  # type: ignore
        return self._job_queue.count_states()[JobState.COMPLETED]

    def getNumFailed(self) -> int:
        if isinstance(self._job_queue, JobQueue):
            return self._job_queue.count_status(JobStatus.FAILED)  # type: ignore
        return self._job_queue.count_states()[JobState.FAILED]

    def getNumWaiting(self) -> int:
        if isinstance(self._job_queue, JobQueue):
            return self._job_queue.count_status(JobStatus.WAITING)  # type: ignore
        return self._job_queue.count_states()[JobState.WAITING]

    def didRealizationSucceed(self, iens: int) -> bool:
        if isinstance(self._job_queue, JobQueue):
            queue_index = self.get_run_args(iens).queue_index
            if queue_index is None:
                raise ValueError("Queue index not set")
            return (
                self._job_queue.job_list[queue_index].queue_status == JobStatus.SUCCESS
            )
        if iens in self._job_queue._jobs:
            return self._job_queue._jobs[iens].state == JobState.COMPLETED
        return False

    def didRealizationFail(self, iens: int) -> bool:
        # For the purposes of this class, a failure should be anything (killed
        # job, etc) that is not an explicit success.
        return not self.didRealizationSucceed(iens)

    def isRealizationFinished(self, iens: int) -> bool:
        if isinstance(self._job_queue, JobQueue):
            run_arg = self.get_run_args(iens)

            queue_index = run_arg.queue_index
            if queue_index is not None:
                return not (
                    self._job_queue.job_list[queue_index].is_running()
                    or self._job_queue.job_list[queue_index].queue_status
                    == JobStatus.WAITING
                )
            else:
                # job was not submitted
                return False

        if iens not in self._job_queue._jobs:
            return False
        state_to_finished_or_not = {
            JobState.WAITING: False,
            JobState.SUBMITTING: False,
            JobState.PENDING: False,
            JobState.RUNNING: False,
            JobState.ABORTING: False,
            JobState.COMPLETED: True,
            JobState.FAILED: True,
            JobState.ABORTED: True,
        }
        return state_to_finished_or_not[self._job_queue._jobs[iens].state]

    def __repr__(self) -> str:
        if not isinstance(self._job_queue, JobQueue):
            raise NotImplementedError
        running = "running" if self.isRunning() else "not running"
        numRunn = self.getNumRunning()
        numSucc = self.getNumSuccess()
        numFail = self.getNumFailed()
        numWait = self.getNumWaiting()
        return (
            f"SimulationContext({running}, #running = {numRunn}, "
            f"#success = {numSucc}, #failed = {numFail}, #waiting = {numWait})"
        )

    def get_ensemble(self) -> Ensemble:
        return self._run_context.ensemble

    def stop(self) -> None:
        self._job_queue.kill_all_jobs()
        self._sim_thread.join()

    def job_progress(self, iens: int) -> Optional[ForwardModelStatus]:
        """Will return a detailed progress of the job.

        The progress report is obtained by reading a file from the filesystem,
        that file is typically created by another process running on another
        machine, and reading might fail due to NFS issues, simultanoues write
        and so on. If loading valid json fails the function will sleep 0.10
        seconds and retry - eventually giving up and returning None. Also for
        jobs which have not yet started the method will return None.

        When the method succeeds in reading the progress file from the file
        system the return value will be an object with properties like this:

            progress.start_time
            progress.end_time
            progress.run_id
            progress.jobs = [
                (job1.name, job1.start_time, job1.end_time, job1.status, job1.error_msg),
                (job2.name, job2.start_time, job2.end_time, job2.status, job2.error_msg),
                (jobN.name, jobN.start_time, jobN.end_time, jobN.status, jobN.error_msg)
            ]
        """  # noqa
        run_arg = self.get_run_args(iens)

        if isinstance(self._job_queue, JobQueue):
            queue_index = run_arg.queue_index
            if queue_index is None:
                # job was not submitted
                return None
            if self._job_queue.job_list[queue_index].queue_status == JobStatus.WAITING:
                return None
        else:
            if (
                iens not in self._job_queue._jobs
                or self._job_queue._jobs[iens].state == JobState.WAITING
            ):
                return None
        return ForwardModelStatus.load(run_arg.runpath)

    def run_path(self, iens: int) -> str:
        """
        Will return the path to the simulation.
        """
        return self.get_run_args(iens).runpath

    def job_status(self, iens: int) -> Optional["JobStatus"]:
        """Will query the queue system for the status of the job."""
        if isinstance(self._job_queue, JobQueue):
            run_arg = self.get_run_args(iens)
            queue_index = run_arg.queue_index
            if queue_index is None:
                # job was not submitted
                return None
            int_status = self._job_queue.job_list[queue_index].queue_status
            return JobStatus(int_status)
        state_to_legacy = {
            JobState.WAITING: JobStatus.WAITING,
            JobState.SUBMITTING: JobStatus.SUBMITTED,
            JobState.PENDING: JobStatus.PENDING,
            JobState.RUNNING: JobStatus.RUNNING,
            JobState.ABORTING: JobStatus.DO_KILL,
            JobState.COMPLETED: JobStatus.SUCCESS,
            JobState.FAILED: JobStatus.FAILED,
            JobState.ABORTED: JobStatus.IS_KILLED,
        }
        return state_to_legacy[self._job_queue._jobs[iens].state]
