import os

from dotenv import load_dotenv

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