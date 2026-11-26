from unittest.mock import patch

import pytest
import requests

from src.weather_api import get_weather


@patch("src.weather_api.requests.get")
def test_get_weather(mock_get):
    mock_get.return_value.json.return_value = {
        "city": "Toronto",
        "temperature": 15,
    }

    result = get_weather("Toronto")

    assert result["city"] == "Toronto"
    assert result["temperature"] == 15

    mock_get.assert_called_once_with(
        "https://example.com/weather",
        params={"city": "Toronto"},
        timeout=30,
    )


@patch("src.weather_api.requests.get")
def test_api_failure(mock_get):
    mock_get.return_value.raise_for_status.side_effect = requests.HTTPError(
        "API unavailable"
    )

    with pytest.raises(requests.HTTPError):
        get_weather("Toronto")
