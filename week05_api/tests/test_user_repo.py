import pytest
import requests
from unittest.mock import Mock
from src.user_repo import get_active_users_count

def test_returns_count_of_active_users(mocker):
    fake_response = Mock()
    fake_response.json.return_value = [
    {"id": 1, "name": "Igor", "is_active": True},
    {"id": 2, "name": "Anna", "is_active": True},
    {"id": 3, "name": "Bob", "is_active": True},
    {"id": 4, "name": "Charlie", "is_active": False},
    {"id": 5, "name": "Dave", "is_active": False},
]

    mock_get = mocker.patch('src.user_repo.requests.get')
    mock_get.return_value = fake_response

    result = get_active_users_count()

    assert result == 3, f'Expected 3, got {result}'
    mock_get.assert_called_once_with("https://api.com/users", timeout=5)


def test_returns_zero_on_connection_error(mocker):
    mock_get = mocker.patch('src.user_repo.requests.get')
    mock_get.side_effect = requests.ConnectionError('Bad Connect')

    result = get_active_users_count()

    assert result == 0, f'Expected 0, got {result}'


def test_returns_zero_on_empty_users(mocker):
    fake_response = Mock()
    fake_response.json.return_value = []

    mock_get = mocker.patch('src.user_repo.requests.get')
    mock_get.return_value = fake_response

    result = get_active_users_count()

    assert result == 0, f'Expected 0, got {result}'