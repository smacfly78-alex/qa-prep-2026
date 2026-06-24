import pytest
from src.functions import word_frequency, countdown, calculate_score, is_palindrome


def test_word_frequency_counts_correctly() -> None:
    phrase = "the quick brown fox"
    result = word_frequency(phrase)
    assert result == {"the": 1, "quick": 1, "brown": 1, "fox": 1}

def test_word_frequency_is_case_insensitive() -> None:
    phrase = "The THE the"
    result = word_frequency(phrase)
    assert result["the"] == 3

@pytest.mark.parametrize('phrase, expected', [
    ("the quick brown fox", {"the": 1, "quick": 1, "brown": 1, "fox": 1}),
    ("The THE the", {"the": 3}),
    ("", {}),
    ("hello", {"hello": 1})
])
def test_word_frequency(phrase: str, expected: dict[str, int]) -> None:
    result = word_frequency(phrase)
    assert result == expected

def test_countdown_yields_correct_values() -> None:
    items = list(countdown(5))
    assert items == [5, 4, 3, 2, 1]

def test_calculate_score_returns_correct_percentage() -> None:
    result = calculate_score(8, 10)
    assert result == 80.0

def test_calculate_score_raises_on_zero_total() -> None:
    with pytest.raises(ValueError):
        calculate_score(8, 0)

def test_calculate_score_raises_on_negative_correct() -> None:
    with pytest.raises(ValueError, match="negative"):
        calculate_score(-1, 10)

def test_calculate_score_raises_when_correct_exceeds_total() -> None:
    with pytest.raises(ValueError, match="exceed"):
        calculate_score(15, 10)

@pytest.mark.parametrize('input_text, expected', [('anna', True), ('Anna', True), ('A man, a plan, a canal: Panama', True),
                                                  ('hello', False), ('', True)])
def test_is_palindrome(input_text: str, expected: bool) -> None:
    assert is_palindrome(input_text) == expected


@pytest.mark.parametrize("correct,total,match_text", [
    (8, 0, "positive"),
    (-1, 10, "negative"),
    (15, 10, "exceed"),
])
def test_calculate_score_raises(correct: int,total: int, match_text: str) -> None:
    with pytest.raises(ValueError, match=match_text):
        calculate_score(correct,total)
