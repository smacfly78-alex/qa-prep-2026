from unittest.mock import Mock

import pytest
import requests

from week06_api.src.retry_practice import fetch_data_with_retry


def test_fetch_data_success_first_try(mocker):
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {"result": "ok"}

    mock_get = mocker.patch("week06_api.src.retry_practice.requests.get")
    mock_get.return_value = fake_response

    result = fetch_data_with_retry("https://api.com/data")
    expected = {"result": "ok"}

    assert result == expected, f'Expected {expected}, got {result}'
    assert mock_get.call_count == 1, f'Expected 1, got {mock_get.call_count}'

def test_fetch_data_succeeds_after_retry(mocker):
    fake_response = Mock()
    fake_response.json.return_value = {"result": "ok"}

    mock_get = mocker.patch("week06_api.src.retry_practice.requests.get")
    mock_get.side_effect = [requests.ConnectionError("fail"), requests.ConnectionError("fail"), fake_response]

    result = fetch_data_with_retry("https://api.com/data")
    expected = {"result": "ok"}

    assert result == expected, f'Expected {expected}, got {result}'
    assert mock_get.call_count == 3, f'Expected 3, got {mock_get.call_count}'

def test_fetch_data_fails_after_max_retries(mocker):
    mock_get = mocker.patch("week06_api.src.retry_practice.requests.get")
    mock_get.side_effect = [requests.ConnectionError("fail"), requests.ConnectionError("fail"),
                            requests.ConnectionError("fail")]

    with pytest.raises(requests.ConnectionError):
        fetch_data_with_retry("https://api.com/data")

    assert mock_get.call_count == 3, f'Expected 3, got {mock_get.call_count}'
