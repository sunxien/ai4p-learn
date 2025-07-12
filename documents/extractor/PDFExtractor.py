# System Libs
import pymupdf # imports the pymupdf library
import time

# Project Modules
from pylang.logger import Logger
from pylang.utils import Utils

logger = Logger.get_root_logger()

def read_pdf_file(file: str):
  begin = time.perf_counter()
  try:
    contents = []
    pages = pymupdf.open(file) # open a document
    for (index, page) in enumerate(pages): # iterate the document pages
      text = page.get_text() # get plain text encoded as UTF-8
      contents.append(text)
    return contents
  finally:
    elapsed = round(time.perf_counter()-begin, 2)
    logger.info(f"Read \"{file}\" success. Elapsed: {elapsed}s")

# Main
if __name__ == "__main__":
  read_pages = read_pdf_file("../resources/prompt_template_en.pdf")
  for (page_no, read_page) in enumerate(read_pages):
      logger.info(f"{read_page}")
      logger.info(f"{Utils.repeat_star(64)} Page.{page_no} {Utils.repeat_star(64)}")