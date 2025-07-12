import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

from pylang.utils import Utils
from pylang.logger import Logger

logger = Logger.get_root_logger()
logger.INFO(f"{Utils.filepath(__file__)} init....")

