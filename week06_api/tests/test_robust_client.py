from unittest.mock import Mock

import pytest
import requests

from week06_api.src.robust_client import robust_fetch


def test_success_first_try(mocker):
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {"data": "ok"}

    mock_session_class = mocker.patch('week06_api.src.robust_client.requests.Session')
    mock_session_instance = mock_session_class.return_value
    mock_session_instance.get.return_value = fake_response

    result = robust_fetch("https://api.example.com/data", "test_token_123")

    expected = {"data": "ok"}
    assert result == expected, f'Expected {expected}, got {result}'
    assert mock_session_instance.get.call_count == 1, f'Expected 1, got {mock_session_instance.get.count_call}'

def test_success_after_retry(mocker):
    fake_response_200 = Mock()
    fake_response_200.status_code = 200
    fake_response_200.json.return_value = {"data": "ok"}

    mock_session_class = mocker.patch('week06_api.src.robust_client.requests.Session')
    mock_session_instance = mock_session_class.return_value
    mock_session_instance.get.side_effect = [requests.ConnectionError, requests.ConnectionError, fake_response_200]

    result = robust_fetch("https://api.example.com/data", "test_token_123")

    expected = {"data": "ok"}
    assert result == expected, f'Expected {expected}, got {result}'
    assert mock_session_instance.get.call_count == 3, f'Expected 3, got {mock_session_instance.get.count_call}'


def test_http_error_returns_none(mocker):
    fake_response = Mock()
    fake_response.raise_for_status.side_effect = requests.HTTPError("404")
    fake_response.status_code = 404

    mock_session_class = mocker.patch('week06_api.src.robust_client.requests.Session')
    mock_session_instance = mock_session_class.return_value
    mock_session_instance.get.return_value = fake_response

    result = robust_fetch("https://api.example.com/data", "test_token_123")

    assert result is None, f'Expected None, got {result}'
    assert mock_session_instance.get.call_count == 1, f'Expected 1, got {mock_session_instance.get.count_call}'


def test_all_retries_fail(mocker):
    mock_session_class = mocker.patch('week06_api.src.robust_client.requests.Session')
    mock_session_instance = mock_session_class.return_value
    mock_session_instance.get.side_effect = [requests.ConnectionError, requests.ConnectionError, requests.ConnectionError]

    with pytest.raises(requests.ConnectionError):
        robust_fetch("https://api.example.com/data", "test_token_123")

    assert mock_session_instance.get.call_count == 3, f'Expected 3, got {mock_session_instance.get.count_call}'