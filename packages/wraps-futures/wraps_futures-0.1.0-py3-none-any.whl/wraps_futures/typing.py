from typing import Callable, TypeVar

from typing_extensions import ParamSpec

from wraps_futures.either import FutureEither
from wraps_futures.option import FutureOption
from wraps_futures.result import FutureResult

__all__ = ("FutureOptionCallable", "FutureResultCallable", "FutureEitherCallable")

P = ParamSpec("P")

T = TypeVar("T")
E = TypeVar("E")

L = TypeVar("L")
R = TypeVar("R")


FutureOptionCallable = Callable[P, FutureOption[T]]
"""Represents future option callables `(**P) -> FutureOption[T]`."""

FutureResultCallable = Callable[P, FutureResult[T, E]]
"""Represents future result callables `(**P) -> FutureResult[T, E]`."""

FutureEitherCallable = Callable[P, FutureEither[L, R]]
"""Represents future either callables `(**P) -> FutureEither[L, R]`."""
