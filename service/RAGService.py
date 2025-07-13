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

# Current Project Modules
from pymilvus import SearchResult
from pymilvus.client.search_result import HybridHits

from models.local_embedding.M3eBaseEmbedding import M3eBaseEmbedding
from documents.extractor.PDFExtractor import read_pdf_file
from documents.extractor.TxTExtractor import read_txt_file
from documents.chunking.TextStructuredBasedChunking import split_content
from models.local_embedding.PyMilvusEmbedding import PyMilvusEmbedding
from vectordb.milvus.Configuration import Configuration
from vectordb.milvus.MilvusOperator import MilvusOperator

from pylang.utils.Utils import current_dir, parent_dir, join_paths
from pylang.logger import Logger

logger = Logger.get_root_logger()

class RAGService:

    collection_name: str

    # todo does it oop?
    embed: M3eBaseEmbedding
    persist: MilvusOperator

    def __init__(self, collection_name: str):
        self.collection_name = collection_name
        self.embed = M3eBaseEmbedding()
        self.persist = MilvusOperator(Configuration(True))

    def load_documents(self, filetype: str, filepath: str):
        if filetype == "pdf":
            contents = read_pdf_file(filepath)
            chunks = split_content("\n\n".join(contents))
            vectors = self.embed.embedding_documents(chunks)
            self.persist.insert_documents(self.collection_name, vectors)
        elif filetype == "txt":
            contents = read_txt_file(filepath)
            chunks = split_content("\n\n".join(contents))
            vectors = self.embed.embedding_documents(chunks)
            self.persist.insert_documents(self.collection_name, vectors)
        else:
            raise RuntimeError(f"filetype: {filetype} is unsupported")


    def search_knowledge(self, query: str):
        query_vectors = self.embed.embedding_query(query)
        related_docs = self.persist.search_documents(self.collection_name, query_vectors)

        related_contents = []
        for related_doc in related_docs:
            if type(related_doc) == HybridHits:
                for sub_related_doc in related_doc:
                    related_contents.append(sub_related_doc.entity.text)
            else:
                raise RuntimeError(f"not HybridHits type")

        for related_content in related_contents:
            logger.info(related_content)

        # todo prepare prompt template
        # todo send to LLM
        # todo agent, function call, mcp


if __name__ == "__main__":
    hot_news = join_paths(parent_dir(current_dir()), "documents", "resources", "hot_news.txt")
    logger.info(hot_news)

    rag_service = RAGService("ai4p")
    rag_service.load_documents("txt", hot_news)
    rag_service.search_knowledge("体育")