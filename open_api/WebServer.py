# External Modules
from fastapi import FastAPI
import uvicorn

# Current Project Modules
from pylang.logger import Logger
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
