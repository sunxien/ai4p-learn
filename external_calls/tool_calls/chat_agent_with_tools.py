import json
import os

from openai import OpenAI
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

client = OpenAI(
    # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope SDK的base_url
)

tools=[
    {
        "type": "function",
        "function": {
            "name": "get_current_datetime",
            "description": "获取当前的日期时间",
            "parameters": {
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_today_weather",
            "description": "获取今天给定城市的天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市或区，例如：北京，海淀区"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

# 封装模型响应函数
def get_completion(messages):
    completion = client.chat.completions.create(
        model="qwen-max",
        messages=messages,
        tools=tools
    )
    print(completion.model_dump_json(indent=4))
    return completion.model_dump()


def chat_with_qwen_max():
    print('\n')
    messages = [
        {
            "role": "user",
            "content": input('请输入您想要咨询的问题：')
        }
    ]
    print("-" * 60)

    # ***************************** 模型的第一轮调用 *****************************
    i = 1
    first_response = get_completion(messages)
    assistant_output = first_response['choices'][0]['message']
    print(f"\n第{i}轮大模型交互响应：{first_response}\n")

    if assistant_output['content'] is None:
        assistant_output['content'] = ""
    messages.append(assistant_output)

    # 如果不需要调用工具，则直接返回最终答案
    if assistant_output['tool_calls'] == None:  # 如果模型判断无需调用工具，则将assistant的回复直接打印出来，无需进行模型的第二轮调用
        print(f"无需调用工具，直接回复：{assistant_output['content']}")
        return

    # 如果需要调用工具，则进行模型的多轮调用，直到模型判断无需调用工具
    while assistant_output['tool_calls'] != None:
        tool_info = {"name": "", "role": "tool", "content": "目前没有调用任何工具！"}

        first_function=assistant_output['tool_calls'][0]['function']
        if first_function['name'] == 'get_today_weather':
            location = json.loads(first_function['arguments'])['location']
            tool_info["name"] = "get_today_weather"
            tool_info['content'] = WeatherService().get_today_weather(location)

        elif first_function['name'] == 'get_current_time':
            tool_info["name"]="get_current_time"
            tool_info['content'] = utils.get_current_time()

        print(f"工具输出信息：{tool_info['content']}\n")
        print("-" * 60)
        messages.append(tool_info)

        assistant_output = get_completion(messages)['choices'][0]['message']
        if assistant_output['content'] is None:
            assistant_output['content'] = ""

        messages.append(assistant_output)
        i += 1
        print(f"第{i}轮大模型交互响应：{assistant_output}\n")

    # ********************************************************************************
    print(f"最终答案：{assistant_output['content']}")


# Main
if __name__ == "__main__":

    while True:
        chat_with_qwen_max()