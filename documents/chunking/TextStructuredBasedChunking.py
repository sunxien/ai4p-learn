# Text-structured based
# Text is naturally organized into hierarchical units such as paragraphs, sentences, and words.
# We can leverage this inherent structure to inform our splitting strategy,
# creating split that maintain natural language flow, maintain semantic coherence within split,
# and adapts to varying levels of text granularity. LangChain's RecursiveCharacterTextSplitter implements this concept:
#
# The RecursiveCharacterTextSplitter attempts to keep larger units (e.g., paragraphs) intact.
# If a unit exceeds the chunk size, it moves to the next level (e.g., sentences).
# This process continues down to the word level if necessary.

# External Modules
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Current Project Modules
from documents.resources import Resources
from pylang.logger import Logger
from pylang.utils import Utils

logger = Logger.get_root_logger()

def split_content(content: str):
    return RecursiveCharacterTextSplitter(
        separators=["\n", "\n\n"],
        chunk_size=30,
        chunk_overlap=2
    ).split_text(content)


# Document
def split_documents(documents: list):
    return RecursiveCharacterTextSplitter(
        separators=["\n", "\n\n"],
        chunk_size=30,
        chunk_overlap=2
    ).split_documents(documents)


# Main
if __name__ == "__main__":
    split_docs = split_content(Resources.content)
    for (page_no, split_doc) in enumerate(split_docs):
        logger.info(f"{split_doc}")
        logger.info(f"{Utils.repeat_star(64)} Page.{page_no} {Utils.repeat_star(64)}")
