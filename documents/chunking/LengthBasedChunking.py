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

# Current Project Modules
from resources import Resources
from pylang.logger import Logger
from pylang.utils import Utils

logger = Logger.get_root_logger()

def split_content(content: str):
    return CharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base",
        chunk_size=24,
        chunk_overlap=0
    ).split_text(content)



def split_documents(documents: list):
    return CharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base",
        chunk_size=24,
        chunk_overlap=0
    ).split_documents(documents)



# Main
if __name__ == "__main__":
    split_docs = split_content(Resources.content)
    for (page_no, split_doc) in enumerate(split_docs):
        logger.info(f"{split_doc}")
        logger.info(f"{Utils.repeat_star(64)} Page.{page_no} {Utils.repeat_star(64)}")