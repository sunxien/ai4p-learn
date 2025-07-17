
from pylang.utils.utils import *

RESPONSE_JSON_FILE = join_paths(filedir(__file__),"weather_response.json")

def read_response_json_file():
    if os.path.exists(RESPONSE_JSON_FILE):
        with open(RESPONSE_JSON_FILE, 'r', encoding='utf-8') as jf:
            return jf.read()
    else:
        raise RuntimeError(f"{RESPONSE_JSON_FILE} is not found")


def parse_json_string(json_string: str):
    if json_string and json_string.strip() != "":
        import json
        json_object = json.loads(json_string)
        # print(type(json_object))
        status = json_object['status']
        if status != '200':
            raise RuntimeError(f"HTTP status: {status}")

        city_info = json_object['cityInfo']
        city_name = city_info['parent'] + '/' + city_info['city']

        json_data = json_object['data']
        shidu = json_data['shidu']
        pm25 = json_data['pm25']
        pm10 = json_data['pm10']
        quality = json_data['quality']
        wendu = json_data['wendu']
        ganmao = json_data['ganmao']

        forecast = json_data['forecast']
        for date_forecast in forecast:
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

        yesterday = json_data['yesterday']
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


    else:
        raise RuntimeError(f"json string: {json_string} is invalid")


if __name__  == "__main__":
    response_json_string = read_response_json_file()
    # print(response_json_string)
    parse_json_string(response_json_string)
