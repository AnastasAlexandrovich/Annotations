from typing import Dict, List, Final, Optional, Union, TypeVar


# Modify `foo` so it takes an argument of arbitrary type.
def arbitrary_foo(i):
    pass


# foo should accept a dict argument, both keys and values are string.
def dict_foo(x: Dict[str, str]):
    pass


# Make sure `my_list` cannot be re-assigned to.
my_list: Final[list] = []


# `foo` takes keyword arguments of type integer or string.
def kwargs_foo(**kwargs: str | int):
    pass


# foo should accept a list argument, whose elements are string.
def list_foo(x: list[str]):
    pass


# foo can accept an integer argument, None or no argument at all.
def foo(x: Optional[int] = None):
    print(x)


# foo should accept an integer argument.
def int_foo(x: int):
    pass


# foo should return an integer argument.
def return_foo() -> int:
    return 1


# foo should accept a tuple argument, 1st item is a string, 2nd item is an integer.
def tuple_foo(x: tuple[str, int]):
    pass


# Create a new type called Vector, which is a list of float.
type Vector = list[float]


# foo should accept an argument that's either a string or integer.
def union_foo(x: Union[str, int]):
    pass


# `a` should be an integer.
from typing import Any
a: int
