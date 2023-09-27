import sys
import typing

from .app import cli


def main() -> typing.NoReturn:
    """
    Entry point.

    Raises:
        SystemExit: If the application is terminated
    """
    main_app = cli.ExampleCliApp()
    main_app.set_args(*sys.argv[1:])
    sys.exit(main_app.run())


if __name__ == '__main__':
    main()
