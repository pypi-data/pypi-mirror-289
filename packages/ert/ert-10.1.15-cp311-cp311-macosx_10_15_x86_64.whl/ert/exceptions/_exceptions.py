class ErtError(Exception):
    """Base class for exceptions in this module."""

    pass


class StorageError(ErtError):
    def __init__(self, message: str) -> None:
        self.message = message
