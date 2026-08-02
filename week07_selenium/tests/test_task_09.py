from unittest.mock import Mock

from week07_selenium.src.task_09_retry_api import fetch_data


def test_success_first_try(mocker):
    fake_response = Mock()
    fake_response.json.return_value = {"data": "ok"}
    fake_response.status_code = 200

    mock_get = mocker.patch('week07_selenium.src.task_09_retry_api.requests.get')
    mock_get.return_value = fake_response

    result = fetch_data("https://api.com/data")
    assert result == {"data": "ok"}
    assert mock_get.call_count == 1

def test_success_after_500(mocker):
    fake_response_1 = Mock()
    fake_response_1.status_code = 500
    fake_response_2 = Mock()
    fake_response_2.status_code = 200
    fake_response_2.json.return_value = {"data": "ok"}

    mock_get = mocker.patch('week07_selenium.src.task_09_retry_api.requests.get')
    mock_get.side_effect = [fake_response_1, fake_response_2]

    result = fetch_data("https://api.com/data")
    assert result == {"data": "ok"}
    assert mock_get.call_count == 2
