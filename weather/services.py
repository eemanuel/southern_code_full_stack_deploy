from requests.exceptions import RequestException

from southern_code.settings import WEATHER_SERVICE_KEY
from weather.constants import GET
from weather.country_codes import COUNTRY_CODES_MAPPER
from weather.requesters import WeatherRequester


class WeatherService:
    requester = WeatherRequester()
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):  # This converts the class in a singleton.
        if isinstance(cls._instance, cls):
            return cls._instance
        cls._instance = super().__new__(cls)
        return cls._instance

    def get_data(self, city: str, country: str) -> dict:
        """
        Send request to service url, parse the response and return clened data.
        """
        if country:
            country = country.lower()
            country_code = country if len(country) == 2 else COUNTRY_CODES_MAPPER.get(country)
            q_value = f"{city},{country_code}"
        else:
            q_value = city
        url_path = f"/weather?q={q_value}&appid={WEATHER_SERVICE_KEY}&units=metric"

        error_data = {"error": "Error with external service"}
        try:
            response = self.requester.send_request(GET, url_path)
        except RequestException:
            return error_data

        if response.status_code != 200:
            return error_data
        data = self._parse(response.json())
        return data

    @staticmethod
    def _parse(payload):
        city_name = payload.get("name", "")

        sys = payload.get("sys", dict())
        country = sys.get("country", "")

        main = payload.get("main", dict())
        current_temp = main.get("temp")
        current_temp = current_temp if current_temp else ""
        feels_like = main.get("feels_like")
        feels_like = feels_like if feels_like else ""
        temp_max = main.get("temp_max")
        temp_max = temp_max if temp_max else ""
        temp_min = main.get("temp_min")
        temp_min = temp_min if temp_min else ""
        humidity = main.get("humidity", "")
        pressure = main.get("pressure", "")

        weather_payload = payload.get("weather")
        weathers = list()
        for item in weather_payload:
            desc = item.get("description", "")
            desc = desc[0].upper() + desc[1:]
            dictionary = {"main": item.get("main", ""), "description": desc}
            weathers.append(dictionary)

        clouds = payload.get("clouds", dict())
        clouds_percent = clouds.get("all", "")

        wind = payload.get("wind", dict())
        wind_deg = wind.get("def", "")
        wind_speed = wind.get("speed", "")

        # fmt: off
        cleaned_payload = {
            "city_name": city_name, "country": country,
            "current_temp": current_temp, "feels_like": feels_like,
            "temp_max": temp_max, "temp_min": temp_min,
            "humidity": humidity, "pressure": pressure,
            "weathers": weathers, "clouds_percent": clouds_percent,
            "wind_deg": wind_deg, "wind_speed": wind_speed,
        }
        # fmt: on
        return cleaned_payload
