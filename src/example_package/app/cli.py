import enum
import sys
import traceback

from . import base


class ExampleCliApp(base.ApplicationBase):
    """
    Example CLI Application class.
    """

    def run(self) -> int:
        """
        [override]Run application.

        Returns:
            int: Exit code returned to system
        """
        try:
            if(len(self._args) < 1):
                print('One or more arguments required.', file=sys.stderr)
                return self.ExitCode.INVALID_ARGUMENTS
            for line in self._args:
                print(line)
            return self.ExitCode.SUCCESS
        except:
            try:
                traceback.print_exc()
            except:
                pass
            return self.ExitCode.UNKNOWN_ERROR


    class ExitCode(enum.IntEnum):
        """
        Example CLI Application exit code.
        """

        SUCCESS = 0
        """
        Successful termination.
        """
        UNKNOWN_ERROR = 1
        """
        Termination due to unexpected exception.
        """
        INVALID_ARGUMENTS = 2
        """
        Termination due to invalid arguments.
        """
