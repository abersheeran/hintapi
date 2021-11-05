from typing import Callable

from typedweb.utils.register import RegisterDict


def test_register_dict():
    d: RegisterDict[str, Callable] = RegisterDict()

    @d.register("foo")
    def foo():
        pass

    assert d["foo"] is foo
