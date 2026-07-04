from unittest import result

import requests
from unittest.mock import Mock
from week05_api.src.user_service import fetch_user_name, fetch_user_name_safe, fetch_and_notify


def test_user_service(mocker):
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {"name": "Igor", "email": "i@x.com"}

    mock_get = mocker.patch("week05_api.src.user_service.requests.get")
    mock_get.return_value = fake_response

    result = fetch_user_name(123)

    assert result == "Igor"


def test_fetch_user_name_safe_returns_none_on_connection_error(mocker):
    mock_get = mocker.patch("week05_api.src.user_service.requests.get")
    mock_get.side_effect = requests.ConnectionError('Network down')

    result = fetch_user_name_safe(123)

    assert result is None

def test_fetch_user_name_safe_returns_none_on_timeout(mocker):
    mock_get = mocker.patch("week05_api.src.user_service.requests.get")
    mock_get.side_effect = requests.Timeout

    result = fetch_user_name_safe(123)

    assert result is None

def test_fetch_user_name_calls_correct_url(mocker):
    fake_response = Mock()
    fake_response.json.return_value = {"name": "Igor"}

    mock_get = mocker.patch("week05_api.src.user_service.requests.get")
    mock_get.return_value = fake_response

    result = fetch_user_name(456)

    assert result == "Igor"

    mock_get.assert_called_once_with(
        "https://api.example.com/users/456",
        timeout=5
    )

def test_fetch_and_notify_success(mocker):
    fake_response = Mock()
    fake_response.json.return_value = {"name": "Igor"}

    mock_send = mocker.patch('week05_api.src.sms_client.send_sms')
    mock_get = mocker.patch("week05_api.src.user_service.requests.get")
    mock_get.return_value = fake_response

    result = fetch_and_notify(123, "+79001234567")

    assert result is True, f"Expected True, got {result}"
    mock_send.assert_called_once_with("+79001234567", "Hello, Igor!")

def test_fetch_and_notify_returns_false_on_connection_error(mocker):
    mock_get = mocker.patch("week05_api.src.user_service.requests.get")
    mock_get.side_effect = requests.ConnectionError('Bad connect')
    mock_send = mocker.patch('week05_api.src.sms_client.send_sms')

    result = fetch_and_notify(123, "+79001234567")

    assert result is False, f"Expected False, got {result}"
    mock_send.assert_not_called()