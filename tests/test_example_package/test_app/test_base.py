import typing

import pytest

import example_package.app.base as module


@pytest.mark.parametrize(
    ('expected_instans_class', 'expected_instance_args'),
    [
        (module.ApplicationBase, ()),
    ]
)
def test_ApplicationBase_constructor__creates_instance(expected_instans_class: typing.Type,
                                                       expected_instance_args: tuple[str]) -> None:
    actual_instance = module.ApplicationBase()
    assert isinstance(actual_instance, expected_instans_class)
    assert actual_instance._args == expected_instance_args

@pytest.mark.parametrize(
    ('in_set_args_args', 'expected_args'),
    [
        ((), ()),
        (('one two three',), ('one two three',)),
        (('one', 'two', 'three'), ('one', 'two', 'three')),
    ]
)
def test_ApplicationBase_set_args__sets_instance_values(in_set_args_args: tuple[str],
                                                        expected_args: tuple[str]) -> None:
    instance = module.ApplicationBase()
    instance.set_args(*in_set_args_args)
    actual_args = instance._args
    assert actual_args == expected_args

@pytest.mark.parametrize(
    ('in_set_args_args', 'expected_return'),
    [
        ((), module.ApplicationBase.ExitCode.SUCCESS),
    ]
)
def test_ApplicationBase_run__runs_instance(in_set_args_args: tuple[str],
                                            expected_return: int) -> None:
    instance = module.ApplicationBase()
    instance.set_args(*in_set_args_args)
    actual_return = instance.run()
    assert actual_return == expected_return
