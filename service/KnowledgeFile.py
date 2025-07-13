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

import os

def validate_filetype(filetype: str):
    if filetype != "pdf" and filetype != "txt":
        raise RuntimeError(f"filetype: {filetype} is unsupported")
    return filetype


def validate_filepath(filepath: str):
    if not filepath or filepath.strip() == "":
        raise RuntimeError(f"filetype: {filepath} is invalid")
    if not os.path.exists(filepath):
        raise RuntimeError(f"filetype: {filepath} is not exists")
    return filepath


class KnowledgeFile:

    filetype: str
    filepath: str

    def __init__(self, filetype: str, filepath: str):
        self.filetype = validate_filetype(filetype)
        self.filepath = validate_filepath(filepath)


