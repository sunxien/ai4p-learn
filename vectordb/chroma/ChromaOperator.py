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

# System Modules
import time

# External Modules


# Current Project Modules
from pylang.logger import Logger
from vectordb.chroma.Configuration import Configuration

logger = Logger.get_root_logger()

class ChromaOperator:

    def __init__(self, conf: Configuration):
        pass