import pytest
from src.counter import Counter


@pytest.fixture
def counter_with_reset() -> Counter:
    counter = Counter()
    try:
        yield counter
    finally:
        counter.reset()

def test_increment_once(counter_with_reset: Counter) -> None:
    counter_with_reset.increment()
    assert counter_with_reset.value == 1

def test_increment_multiple_times(counter_with_reset: Counter) -> None:
    for x in range(5):
        counter_with_reset.increment()
    assert counter_with_reset.value == 5

def test_initial_state_is_zero(counter_with_reset: Counter) -> None:
    assert counter_with_reset.value == 0