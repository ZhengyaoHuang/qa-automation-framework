from weather import get_weather
import pytest

def test_get_weather(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temp": 25, "condition": "sunny"}

    result = get_weather("New York")
    assert result == {"temp": 25, "condition": "sunny"}
    mock_get.assert_called_once_with("http://api.weatherapi.com/v1/New York")