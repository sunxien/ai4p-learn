# Length-based
# The most intuitive strategy is to split documents based on their length.
# This simple yet effective approach ensures that each chunk doesn't exceed a specified size limit.
# Key benefits of length-based splitting:
#
# Straightforward implementation
# Consistent chunk sizes
# Easily adaptable to different model requirements
# Types of length-based splitting:
#
# Token-based: Splits text based on the number of tokens, which is useful when working with language models.
# Character-based: Splits text based on the number of characters, which can be more consistent across different types of text.

# External Modules
from langchain_text_splitters import CharacterTextSplitter
from huggingface_hub import hf_hub_download

# Current Project Modules
from documents.resources import Resources
from pylang.logger import Logger
from pylang.utils import Utils

logger = Logger.get_root_logger()

def split_content(content: str):
    return CharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base",
        chunk_size=100,
        chunk_overlap=0
    ).split_text(content)

def split_documents(contents: list):
    return CharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base",
        chunk_size=128,
        chunk_overlap=16
    ).split_documents(contents)

# Main
if __name__ == "__main__":
    split_docs = split_content(Resources.content)
    for (page_no, split_doc) in enumerate(split_docs):
        logger.info(f"{split_doc}")
        logger.info(f"{Utils.repeat_star(64)} Page.{page_no} {Utils.repeat_star(64)}")