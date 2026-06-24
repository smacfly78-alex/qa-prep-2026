import pytest

from src.merge_dicts import merge_dicts

def test_merge_dicts_has_three_keys(sample_dicts: list[dict[str, int]]) -> None:
    assert len(merge_dicts(sample_dicts).keys()) == 3

def test_merge_dicts_sums_repeated_keys(sample_dicts: list[dict[str, int]]) -> None:
    assert merge_dicts(sample_dicts) == {"a": 11, "b": 5, "c": 9}

def test_merge_dicts_empty_list_returns_empty_dict() -> None:
    assert merge_dicts([]) == {}

@pytest.mark.parametrize("input_dicts,expected", [
    ([{"a": 1}, {"a": 2}], {"a": 3}),
    ([], {}),
    ([{"x": 5}], {"x": 5}),
    ([{"a": 1, "b": 2}, {"b": 3}], {"a": 1, "b": 5}),
])
def test_merge_dicts_various_inputs(input_dicts, expected) -> None:
    assert merge_dicts(input_dicts) == expected


