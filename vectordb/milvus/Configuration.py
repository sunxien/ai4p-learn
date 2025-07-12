
# External Modules
from pydantic import BaseModel

# Current Project Modules
from pylang.logger import Logger

logger = Logger.get_root_logger()

class Configuration(BaseModel):

    local: bool = True
    url: str = "http://localhost:19530"
    user: str = "",
    password: str = "",
    db_name: str = "default",
    token: str = "",
    timeout: float = None,

    def __init__(self, local: bool):
        super().__init__()
        self.local = local
        # if not local:
        #     # if not self.url or self.url.strip() == "":
        #     #     raise RuntimeError(f"remove milvus url: {self.url} is invalid")
        #     # if not self.user or self.user.strip() == "":
        #     #     raise RuntimeError(f"remove milvus user: {self.user} is invalid")
        #     # if not self.password or self.password.strip() == "":
        #     #     raise RuntimeError(f"remove milvus password: {self.password} is invalid")
        #     if not self.token or self.token.strip() == "":
        #         raise RuntimeError(f"remove milvus token: {self.token} is invalid")


if __name__ == "__main__":
    try:
        conf = Configuration(False)
    except Exception as e:
        logger.error(type(e).__name__, e.args)



