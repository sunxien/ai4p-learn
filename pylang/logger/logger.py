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

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s:%(thread)d] %(levelname)s %(filename)s[:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
    # filename="ai4p-learn.log"
)

# Filter 3rd party libs
logging.getLogger("httpx").setLevel(logging.WARNING)

class ModuleFilter(logging.Filter):

    def __init__(self, exclude_modules: list):
        super().__init__()
        self.exclude_modules = exclude_modules

    def filter(self, record):
        if not self.exclude_modules or len(self.exclude_modules) == 0:
            return True
        return record.module not in self.exclude_modules


def get_root_logger(*args):
    inner_logger = logging.getLogger("root")
    inner_logger.addFilter(ModuleFilter(args))
    return inner_logger

def get_logger(logger_name: str, *args):
    inner_logger = logging.getLogger(logger_name)
    inner_logger.addFilter(ModuleFilter(args))
    return inner_logger

if __name__ == "__main__":
    logger = get_root_logger()
    logger.info("Hello World")