import orjson

class Response:

    code: int
    data: str = None
    message: str = None

    def __init__(self, code: int, data: str, message: str):
        self.code = code
        self.data = data
        self.message = message

    # Don't extend BaseModel, it may cause error like: object has no attribute '__pydantic_fields_set__'.
    def to_json_string(self):
        return orjson.dumps(self, default=lambda o: o.__dict__)

# Main
if __name__ == "__main__":
    resp = Response(200, "7532.22", "success")
    print(resp.to_json_string())