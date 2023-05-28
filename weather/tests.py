from unittest.mock import patch

from django.test import Client
from django.urls import reverse

from pytest import mark
from requests.exceptions import ConnectionError

MOCKED_DATA = {
    "city_name": "Buenos Aires",
    "clouds_percent": 100,
    "country": "AR",
    "current_temp": 18,
    "feels_like": 17,
    "humidity": 96,
    "latitude": -34.6037,
    "longitude": -58.3816,
    "pressure": 1007,
    "temp_max": 20,
    "temp_min": 15,
    "weathers": [{"description": "Niebla", "main": "Silen Hill"}],
    "wind_deg": None,
    "wind_speed": 14.17,
}


class TestWeatherView:
    client = Client()

    @mark.success
    @patch("weather.services.WeatherService.get_data")
    def test_get_success(self, get_data_mock):
        """Testing template returned with GET from WeatherView."""
        get_data_mock.return_value = MOCKED_DATA

        response = self.client.get(reverse("weather"))
        content = response.content.decode("utf-8")
        assert "weather_form" in content
        assert "weather_info" in content
        assert "City" in content
        assert "Temperature" in content
        assert "Wind" in content
        assert content.count("Temp") == 3
        assert response.status_code == 200

    @mark.success
    @patch("weather.services.WeatherService.get_data")
    def test_post_success(self, get_data_mock):
        """Testing template returned with POST from WeatherView."""
        get_data_mock.return_value = MOCKED_DATA

        data = {"city_name": "Buenos Aires", "country": "Argentina"}
        response = self.client.post(reverse("weather"), data)
        content = response.content.decode("utf-8")
        assert "weather_info" in content
        assert "weather_form" not in content
        assert "City" in content
        assert "Temperature" in content
        assert "Wind" in content
        assert "Buenos Aires" in content
        assert "Niebla" in content
        assert "1007 hPa" in content
        assert "100 %" in content
        assert response.status_code == 200

    @mark.error
    @patch("weather.requesters.WeatherRequester.send_request")
    def test_requester_connection_error(self, send_request_mock):
        """
        Testing if the average is not returned
        when the requester get or post raise a ConnectionError.
        """

        send_request_mock.side_effect = ConnectionError()

        data = {"city_name": "Buenos Aires", "country": "Argentina"}
        response = self.client.post(reverse("weather"), data)
        content = response.content.decode("utf-8")
        assert "Error with external service" in content
        assert response.status_code == 200
