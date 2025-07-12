from pylang.utils import Utils
from pylang.logger import Logger

import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

logger = Logger.get_root_logger()
logger.debug(f"{Utils.filepath(__file__)} init....")

