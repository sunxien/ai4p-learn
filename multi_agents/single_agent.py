import os

from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_core.runnables import RunnableWithMessageHistory, RunnableConfig
from langchain_openai import ChatOpenAI

from pydantic import SecretStr

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

LANGSMITH_TRACING="true"
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_PROJECT="ai4p-learn"

llm = ChatOpenAI(
    model="qwen-max",
    api_key=SecretStr(DASHSCOPE_API_KEY), # Expected type 'SecretStr | None', got 'str' instead
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# wikipedia
tools = load_tools(['wikipedia'])

# prompt = hub.pull("hwchase17/react")
prompt = hub.pull("hwchase17/react-chat")
agent = create_react_agent(llm, tools, prompt)

# Stateless
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


# agent_executor.invoke(
#     input={"input": "美国现任总统是谁？", "chat_history": []}
# )

message_history = ChatMessageHistory()
agent_with_chat_history = RunnableWithMessageHistory(
    agent_executor,
    lambda session_id: message_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

runnable_config=RunnableConfig(
    configurable={"configurable": {"session_id": "session-10086"}}
)

agent_with_chat_history.invoke(
    input={"input": "美国现任总统是谁？"},
    config=runnable_config,
)

