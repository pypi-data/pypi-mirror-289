from typing import Optional

from ert import ErtScript
from ert.exceptions import StorageError


class ExportMisfitDataJob(ErtScript):
    """
    Will export misfit per observation and realization to a hdf file.
    The hdf file has the observation as key, and the misfit as values.
    The filename is "misfit.hdf" by default, but can be overridden by giving
    the filename as the first parameter:
    EXPORT_MISFIT_DATA path/to/output.hdf
    The misfit its calculated as follows:
    ((response_value - observation_data) / observation_std)**2
    """

    def run(self, target_file: Optional[str] = None) -> None:
        ert = self.ert()

        if target_file is None:
            target_file = "misfit.hdf"
        if self.ensemble is None:
            raise StorageError("No responses loaded")

        realizations = self.ensemble.get_realization_list_with_responses()

        from ert import LibresFacade

        facade = LibresFacade(ert)
        misfit = facade.load_all_misfit_data(self.ensemble)
        if not realizations or misfit.empty:
            raise StorageError("No responses loaded")

        misfit.columns = [val.split(":")[1] for val in misfit.columns]
        misfit = misfit.drop("TOTAL", axis=1)
        misfit.to_hdf(target_file, key="misfit", mode="w")
