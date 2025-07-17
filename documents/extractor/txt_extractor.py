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

# System Libs
import time

# Project Modules
from pylang.logger import logger
from pylang.utils import utils

logger = Logger.get_root_logger()

def read_txt_file(file: str):
  begin = time.perf_counter()
  try:
    contents = []
    lines = open(file).readlines()
    for line in lines:
        contents.append(line.strip())
    return contents
  finally:
    elapsed = round(time.perf_counter()-begin, 2)
    logger.info(f"Read \"{file}\" success. Elapsed: {elapsed}s")

# Main
if __name__ == "__main__":
  read_lines = read_txt_file("../../resources/hot_news.txt")
  for (page_no, read_line) in enumerate(read_lines):
      logger.info(f"{read_line}")
      logger.info(f"{utils.repeat_star(64)} Page.{page_no} {utils.repeat_star(64)}")