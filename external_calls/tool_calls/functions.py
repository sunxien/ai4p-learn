import os
from dotenv import load_dotenv

from pylang.utils import utils
from service.weather_service import WeatherService

# You should create DASHSCOPE_API_KEY at bailian.console.aliyun.com
# Add [DASHSCOPE_API_KEY=xxxx] into {HOME_DIR}/.env
dotenv_file=utils.join_paths(utils.home_dir(), ".env")
if not os.path.exists(dotenv_file):
    raise RuntimeError(f"{dotenv_file} is not exists")

load_dotenv(
    dotenv_path=dotenv_file
)

DASHSCOPE_API_KEY=os.getenv("DASHSCOPE_API_KEY")
if not DASHSCOPE_API_KEY:
    raise RuntimeError(f"DASHSCOPE_API_KEY is None. (See: {dotenv_file})")


def get_function_by_name(function_name: str):
    if function_name == "get_current_datetime":
        return utils.get_current_time()
    elif function_name == "get_today_weather":
        return WeatherService().get_today_weather
    else:
        raise RuntimeError(f"unsupported function")


if __name__ == "__main__":
    pass
    # function_call = get_function_by_name("get_current_datetime")
    # result = function_call.__call__()
    # print(f"Call {function_call.__name__} success. Result: {result}")
    #
    # function_call = get_function_by_name("get_today_weather")
    # result = function_call.__call__("佛山")
    # print(f"Call {function_call.__name__} success. Result: {result}")
