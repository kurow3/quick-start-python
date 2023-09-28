import io

import pytest

import example_package.app.cli as module


@pytest.mark.parametrize(
    ('in_set_args_args', 'expected_return', 'expected_stdout', 'expected_stderr'),
    [
        ((), module.ExampleCliApp.ExitCode.INVALID_ARGUMENTS, '', 'One or more arguments required.\n'),
        (('',), module.ExampleCliApp.ExitCode.SUCCESS, '\n', ''),
        ((' ',), module.ExampleCliApp.ExitCode.SUCCESS, ' \n', ''),
        (('one two three',), module.ExampleCliApp.ExitCode.SUCCESS, 'one two three\n', ''),
        (('', '', ''), module.ExampleCliApp.ExitCode.SUCCESS, '\n\n\n', ''),
        ((' ', ' ', ' '), module.ExampleCliApp.ExitCode.SUCCESS, ' \n \n \n', ''),
        (('one', 'two', 'three'), module.ExampleCliApp.ExitCode.SUCCESS, 'one\ntwo\nthree\n', ''),
    ]
)
def test_ExampleCliApp_run__runs_instance(monkeypatch: pytest.MonkeyPatch,
                                          in_set_args_args: tuple[str],
                                          expected_return: int,
                                          expected_stdout: str,
                                          expected_stderr: str) -> None:
    with io.StringIO() as stdout, \
         io.StringIO() as stderr:
        monkeypatch.setattr('sys.stdout', stdout)
        monkeypatch.setattr('sys.stderr', stderr)
        instance = module.ExampleCliApp()
        instance.set_args(*in_set_args_args)
        actual_return = instance.run()
        actual_stdout = stdout.getvalue()
        actual_stderr = stderr.getvalue()
        assert actual_return == expected_return
        assert actual_stdout == expected_stdout
        assert actual_stderr == expected_stderr

@pytest.mark.parametrize(
    ('in_set_args_args', 'expected_return', 'expected_stderr_min_length'),
    [
        (('one', 'two', 'three'), module.ExampleCliApp.ExitCode.UNKNOWN_ERROR, 1),
    ]
)
def test_ExampleCliApp_run__unexpected_exception_occurred(monkeypatch: pytest.MonkeyPatch,
                                                          in_set_args_args: tuple[str],
                                                          expected_return: int,
                                                          expected_stderr_min_length: int) -> None:
    with io.StringIO() as stdout, \
         io.StringIO() as stderr:
        monkeypatch.setattr('sys.stdout', stdout)
        monkeypatch.setattr('sys.stderr', stderr)
        stdout.close()
        instance = module.ExampleCliApp()
        instance.set_args(*in_set_args_args)
        actual_return = instance.run()
        actual_stderr = stderr.getvalue()
        assert actual_return == expected_return
        assert len(actual_stderr) >= expected_stderr_min_length
