import enum


class ApplicationBase(object):
    """
    Application base class.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self._args = ()

    def set_args(self, *args: str) -> None:
        """
        Set arguments.

        Args:
            \*args (str): Arguments passed from system
        """
        self._args = args

    def run(self) -> int:
        """
        Run application.

        Returns:
            int: Exit code returned to system
        """
        return self.ExitCode.SUCCESS


    class ExitCode(enum.IntEnum):
        """
        Application base exit code.
        """

        SUCCESS = 0
        """
        Successful termination.
        """
