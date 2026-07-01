import pytest
from week05_api.src.validation import validate_user_data

@pytest.mark.parametrize("data,expected_missing", [
    ({"id": 1, "name": "Igor", "email": "i@x.com", "age": 30}, []),
    ({"id": 1, "name": "Igor"}, ["email", "age"]),
    ({}, ["id", "name", "email", "age"]),
])
def test_validate_user_data(data: dict, expected_missing: list[str]) -> None:
    result = validate_user_data(data)
    assert result == expected_missing, f'Expected missing: {expected_missing}, got {result}'

