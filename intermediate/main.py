from collections.abc import Awaitable, Callable
from typing import ClassVar, TypeVar, Tuple, Literal, LiteralString, Self, TypedDict, Optional, Required, Unpack


# `run_async` takes an awaitable integer.
def run_async(x: Awaitable[int]):
    pass


# Define a callable type that accepts a string argument and returns None.
SingleStringInput = Callable[[str], None]


# Class `Foo` has a class variable `bar`, which is an integer.
class Foo:
    bar: ClassVar[int]


# Define a decorator that wraps a function and returns a function with the same signature.
F = TypeVar('F', bound=Callable)


def decorator(func: F):
    return func


# For Python >= 3.12
# def decorator[T: Callable](func: T) -> T:
#     return func


# foo should accept an empty tuple argument
def tuple_foo(x: Tuple[()]):
    print(x)


# The function `add` accepts two arguments and returns a value, they all have the same type.
T = TypeVar('T')


def add(a: T, b: T) -> T:
    return a


# For Python >= 3.12
# def add[T](a: T, b: T) -> T:


# The function `add` accepts two arguments and returns a value, they all have the same type.
# The type can only be str or int.
TSI = TypeVar('TSI', str, int)


def generic_add(a: TSI, b: TSI) -> TSI:
    return a


# For Python >= 3.12
# def add[T: (str, int)](a: T, b: T) -> T:


# The function `add` accepts one argument and returns a value, they all have the same type.
# The type can only be int or subclasses of int.
TT = TypeVar('TT', bound=int)


def generic_add2(a: TT) -> TT:
    return a


# For Python >= 3.12
# def add[T: int](a: T) -> T:


# Class `Foo` has an instance variable `bar`, which is an integer.
class FooInstance:
    bar: int


# foo only accepts literal 'left' and 'right' as its argument.
def foo(direction: Literal['left', 'right']):
    pass


# You're writing a web backend.
# Annotate a function `execute_query` which runs SQL, but also can prevent SQL injection attacks.
def execute_query(sql: LiteralString, parameters):
    pass


# `return_self` should return an instance of the same type as the current enclosed class.
# TFoo = TypeVar('TFoo', bound='FooSelf') pass subclass


class FooSelf:
    def return_self(self) -> Self:
        return self

    # def return_self2(self) -> TFoo:
    #     pass


class Student(TypedDict):
    name: str
    age: int
    school: str


# Note: school can be optional
class Student2(TypedDict, total=False):
    name: str
    age: int
    school: Optional[str]


"""
TODO:

Define a class `Person` that represents a dictionary with five string keys:
    name, age, gender, address, email

The value of each key must be the specified type:
    name - str, age - int, gender - str, address - str, email - str

Note: Only `name` is required
"""


class Person(TypedDict, total=False):
    name: Required[str]
    age: int
    gender: str
    address: str
    email: str


# When Unpack is used, type checkers treat kwargs inside the function body as a TypedDict:
"""
TODO:

`foo` expects two keyword arguments - `name` of type `str`, and `age` of type `int`.
"""


class Person2(TypedDict):
    name: str
    age: int


def foo_unpack(**kwargs: Unpack[Person2]):
    pass
