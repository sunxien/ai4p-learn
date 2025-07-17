# Copyright [2025] [Sun Xi'En]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# External Modules
from fastapi import FastAPI
import uvicorn

# Current Project Modules
from pylang.logger import logger
logger = Logger.get_root_logger()

app = FastAPI()

@app.get("/")
async def root():
    return {"code": 200, "message": "Hello World"}

@app.get("/ls/{dirname}")
async def list(dirname: str):
    return {"code": 200, "message": "ls is not allowed"}


# Main: uvicorn WebServer:app --reload
if __name__ == "__main__":
    uvicorn.run(
        app="WebServer:app",
        host="127.0.0.1", port=8000,
        reload=True
    )
