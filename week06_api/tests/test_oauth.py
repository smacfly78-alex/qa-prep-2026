from unittest.mock import Mock, patch

from src.oauth_practice import get_user_data, refresh_access_token


def test_get_user_data_success_first_try(mocker):
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {"id": 1, "name": "Igor"}

    mock_get = mocker.patch("src.oauth_practice.requests.get")
    mock_get.return_value = fake_response

    result = get_user_data(access_token="test_access_token_123",
    refresh_token="test_refresh_token_456")

    expected = {"id": 1, "name": "Igor"}
    assert result == expected, f'Expected {expected}, got {result}'

    assert mock_get.call_count == 1, f'Expected 2, got {mock_get.call_count}'

def test_get_user_data_refreshes_on_401(mocker):
    fake_response_1 = Mock()
    fake_response_1.status_code = 401

    fake_response_2 = Mock()
    fake_response_2.status_code = 200
    fake_response_2.json.return_value = {"id": 1, "name": "Igor"}

    fake_refresh_response = Mock()
    fake_refresh_response.status_code = 200
    fake_refresh_response.json.return_value = {"access_token": "new_access_token"}

    mock_get = mocker.patch("src.oauth_practice.requests.get")
    mock_post = mocker.patch("src.oauth_practice.requests.post")
    mock_post.return_value = fake_refresh_response

    mock_get.side_effect = [fake_response_1, fake_response_2]

    result = get_user_data(access_token="test_access_token_123", refresh_token="test_refresh_token_456")

    expected = {"id": 1, "name": "Igor"}
    assert result == expected, f'Expected {expected}, got {result}'

    assert mock_get.call_count == 2, f'Expected 2, got {mock_get.call_count}'
    assert mock_post.call_count == 1, f'Expected 2, got {mock_post.call_count}'

def test_get_user_data_returns_none_when_refresh_expires(mocker):
    fake_response = Mock()
    fake_response.status_code = 401

    fake_refresh_response = Mock()
    fake_refresh_response.status_code = 401

    mock_get = mocker.patch("src.oauth_practice.requests.get")
    mock_post = mocker.patch("src.oauth_practice.requests.post")

    mock_get.return_value = fake_response
    mock_post.return_value = fake_refresh_response

    result = get_user_data(
        access_token="test_access_token_123",
        refresh_token="test_refresh_token_456"
    )

    assert result is None, f'Expected None, got {result}'
    assert mock_get.call_count == 1, f'Expected 1, got {mock_get.call_count}'
    assert mock_post.call_count == 1, f'Expected 1, got {mock_post.call_count}'