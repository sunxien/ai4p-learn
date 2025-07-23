import os
from operator import itemgetter

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, SecretStr

from pylang.utils import utils

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

# ***********************************************************************
physics_template = """
你是一位非常聪明的物理教授。你擅长以简明易懂的方式回答物理问题。当你不知道某个问题的答案时，你会承认自己不知道。

以下是用户咨询的问题：
{input}
"""

physics_prompt = PromptTemplate.from_template(physics_template)

# ***********************************************************************
math_template = """
你是一个非常优秀的数学家。你擅长回答数学问题。你之所以这么厉害，是因为你能够把难题分解成组成部分，回答这些部分，然后把它们放在一起回答更广泛的问题。

以下是用户咨询的问题：
{input}
"""

math_prompt = PromptTemplate.from_template(math_template)

# ***********************************************************************
general_template = "您是一个很有帮助的助手。尽可能准确地回答用户提出的问题。"

general_prompt = PromptTemplate.from_template(general_template)

from langchain.schema.runnable import RunnableBranch

prompt_branch = RunnableBranch(
    (lambda x: x["topic"] == "物理", physics_prompt),
    (lambda x: x["topic"] == "数学", math_prompt),
    general_prompt
)

# ***********************************************************************
from typing import Literal

class TopicClassifier(BaseModel):
    topic: Literal["物理", "数学", "通用"]

from langchain_core.utils.function_calling import convert_to_openai_function
classifier_function = convert_to_openai_function(TopicClassifier)
print(f"classifier_function: {classifier_function}")

llm = ChatOpenAI(
        model="qwen-max",
        api_key=SecretStr(DASHSCOPE_API_KEY), # Expected type 'SecretStr | None', got 'str' instead
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
      )

llm_runnable = llm.bind(
    functions=[classifier_function],
    function_call={"name": "TopicClassifier"}
)

from langchain.output_parsers.openai_functions import PydanticAttrOutputFunctionsParser
parser = PydanticAttrOutputFunctionsParser(
    pydantic_schema=TopicClassifier,
    attr_name="topic"
)

classifier_chain = llm_runnable | parser

final_chain = (
    RunnablePassthrough.assign(topic=itemgetter("input") | classifier_chain)
    | prompt_branch
    | llm
    | StrOutputParser()
)

response1 = final_chain.invoke({"input": "请问0是奇数还是偶数？"})
print(f"response: {response1}")

response2 = final_chain.invoke({"input": "请解释一下什么是相对论？"})
print(f"response: {response2}")

# 意图识别
if __name__ == "__main__":
    pass