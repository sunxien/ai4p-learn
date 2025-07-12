
# External Modules
from pydantic import BaseModel

# Current Project Modules
from pylang.logger import Logger

logger = Logger.get_root_logger()

class Configuration(BaseModel):

    def __init__(self):
        pass
