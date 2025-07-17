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
from resources import local_resources
from pylang.logger import logger
from pylang.utils import utils

logger = logger.get_root_logger()

def split_content(content: str):
    return RecursiveCharacterTextSplitter(
        separators=["\n", "\n\n"],
        chunk_size=24,
        chunk_overlap=0
    ).split_text(content)


# Document
def split_documents(documents: list):
    return RecursiveCharacterTextSplitter(
        separators=["\n", "\n\n"],
        chunk_size=24,
        chunk_overlap=0
    ).split_documents(documents)


# Main
if __name__ == "__main__":
    split_docs = split_content(local_resources.content)
    for (page_no, split_doc) in enumerate(split_docs):
        logger.info(f"{split_doc}")
        logger.info(f"{utils.repeat_star(64)} Page.{page_no} {utils.repeat_star(64)}")
