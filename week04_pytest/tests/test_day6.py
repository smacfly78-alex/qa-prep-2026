import pytest
from src.day6.task_08_count_by_length import count_words_by_length

@pytest.mark.parametrize("input_text, expected", [
    ("hi hello ok world fox by", {2: 3, 5: 2, 3: 1}),
                         ("cat dog fox", {3: 3}),
                          ("hello", {5: 1}), ("", {})
                          ])

def test_count_words_by_length(input_text: str, expected: dict[int, int]) -> None:
    assert count_words_by_length(input_text) == expected

