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