

class LlmResponse:

    type: str
    message: str

    def __init__(self, type: str, message: str):
        self.type = type
        self.message = message