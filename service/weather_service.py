# System Modules
import json

import requests

# External Modules
from resources.local_resources import *
from pylang.logger import logger

logger = logger.get_root_logger()

def get_weather(city_name: str) -> json:
    city_code = get_city_code(city_name)
    uri = f"http://t.weather.sojson.com/api/weather/city/{city_code}"
    # logger.warning(f"URI: {uri}")
    return json.loads(requests.get(uri).content)

class WeatherService:

    def __init__(self):
        pass

    def get_yesterday_weather(self, city_name: str):
        get_yesterday_weather_response = get_weather(city_name)
        status = get_yesterday_weather_response['status']
        if status != 200:
            raise RuntimeError(f"HTTP status: {status}")

        city_info = get_yesterday_weather_response['cityInfo']
        city_name = city_info['parent'] + '/' + city_info['city']

        yesterday_json_data = get_yesterday_weather_response['data']

        yesterday = yesterday_json_data['yesterday']
        yesterday_date = yesterday['date']
        yesterday_high = yesterday['high']
        yesterday_low = yesterday['low']
        yesterday_ymd = yesterday['ymd']
        yesterday_week = yesterday['week']
        yesterday_sunrise = yesterday['sunrise']
        yesterday_sunset = yesterday['sunset']
        yesterday_aqi = yesterday['aqi']
        yesterday_fx = yesterday['fx']
        yesterday_fl = yesterday['fl']
        yesterday_type = yesterday['type']
        yesterday_notice = yesterday['notice']

        return (city_name + " " + yesterday_ymd + " " + yesterday_week + " " + yesterday_type
                + yesterday_low + " ~ " + yesterday_high + " " +yesterday_fx + " " + yesterday_fl)


    def get_today_weather(self, city_name: str):
        get_today_weather_response = get_weather(city_name)
        status = get_today_weather_response['status']
        if status != 200:
            raise RuntimeError(f"HTTP status: {status}")

        city_info = get_today_weather_response['cityInfo']
        city_name = city_info['parent'] + '/' + city_info['city']

        today_json_data = get_today_weather_response['data']
        today_shidu = today_json_data['shidu']
        today_pm25 = today_json_data['pm25']
        today_pm10 = today_json_data['pm10']
        today_quality = today_json_data['quality']
        today_wendu = today_json_data['wendu']
        today_ganmao = today_json_data['ganmao']

        today_forecast = today_json_data['forecast'][0]
        today_forecast_date = today_forecast['date']
        today_forecast_high = today_forecast['high']
        today_forecast_low = today_forecast['low']
        today_forecast_ymd = today_forecast['ymd']
        today_forecast_week = today_forecast['week']
        today_forecast_sunrise = today_forecast['sunrise']
        today_forecast_sunset = today_forecast['sunset']
        today_forecast_aqi = today_forecast['aqi']
        today_forecast_fx = today_forecast['fx']
        today_forecast_fl = today_forecast['fl']
        today_forecast_type = today_forecast['type']
        today_forecast_notice = today_forecast['notice']

        return (city_name + " " + today_forecast_ymd + " " + today_forecast_week + " " + today_forecast_type
                + today_forecast_low + " ~ " + today_forecast_high + " " +today_forecast_fx + " " + today_forecast_fl)

    def get_two_weeks_forecast_weather(self, city_name: str):
        get_two_weeks_forecast_weather_response = get_weather(city_name)
        status = get_two_weeks_forecast_weather_response['status']
        if status != 200:
            raise RuntimeError(f"HTTP status: {status}")

        city_info = get_two_weeks_forecast_weather_response['cityInfo']
        city_name = city_info['parent'] + '/' + city_info['city']

        two_weeks_forecast_json_data = get_two_weeks_forecast_weather_response['data']

        two_weeks_forecasts = []
        two_weeks_forecast = two_weeks_forecast_json_data['forecast']
        for date_forecast in two_weeks_forecast:
            forecast_date = date_forecast['date']
            forecast_high = date_forecast['high']
            forecast_low = date_forecast['low']
            forecast_ymd = date_forecast['ymd']
            forecast_week = date_forecast['week']
            forecast_sunrise = date_forecast['sunrise']
            forecast_sunset = date_forecast['sunset']
            forecast_aqi = date_forecast['aqi']
            forecast_fx = date_forecast['fx']
            forecast_fl = date_forecast['fl']
            forecast_type = date_forecast['type']
            forecast_notice = date_forecast['notice']
            two_weeks_forecasts.append(
                (forecast_ymd + " " + forecast_week + " " + forecast_type
                 + forecast_low + " ~ " + forecast_high + " " + forecast_fx + " " + forecast_fl)
            )

        return city_name + "\n" + "\n".join(two_weeks_forecasts)


# ****************************************************

# ****************************************************

# Main: https://www.sojson.com/blog/305.html
if __name__ == "__main__":

    response = get_weather("上海")
    # print(response)

    weather_service = WeatherService()

    yesterday_weather = weather_service.get_yesterday_weather("上海")
    logger.warning(f"Yesterday: {yesterday_weather}\n")

    today_weather = weather_service.get_today_weather("上海")
    logger.warning(f"Today: {today_weather}\n")

    two_weeks_forecast_weather = weather_service.get_two_weeks_forecast_weather("上海")
    logger.warning(f"Two weeks forecast: {two_weeks_forecast_weather}\n")