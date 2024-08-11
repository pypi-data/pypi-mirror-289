import pytest
from wraps_core.either import Left, Right
from wraps_futures.either import future_either, future_left, future_right


@pytest.mark.anyio
async def test_future_either() -> None:
    left_value = 13
    right_value = 42

    left = Left(left_value)
    right = Right(right_value)

    assert await future_left(left_value) == await future_either(left)
    assert await future_right(right_value) == await future_either(right)
