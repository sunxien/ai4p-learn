# System Libs
import time

# Project Modules
from pylang.logger import Logger
from pylang.utils import Utils

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
  read_lines = read_txt_file("../resources/hot_news.txt")
  for (page_no, read_line) in enumerate(read_lines):
      logger.info(f"{read_line}")
      logger.info(f"{Utils.repeat_star(64)} Page.{page_no} {Utils.repeat_star(64)}")