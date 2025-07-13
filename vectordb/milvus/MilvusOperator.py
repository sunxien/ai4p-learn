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
from pymilvus import MilvusClient

from models.local_embedding.M3eBaseEmbedding import M3eBaseEmbedding
from models.local_embedding.PyMilvusEmbedding import PyMilvusEmbedding
# Current Project Modules
from pylang.logger import Logger
from pylang.utils.Utils import filepath, join_paths, current_dir, filedir, parent_dir
from vectordb.milvus.Configuration import Configuration

logger = Logger.get_root_logger()

class MilvusOperator:

    client: MilvusClient

    def __init__(self, conf: Configuration):
        begin = time.perf_counter()
        if conf.local:
            db_file = join_paths(filedir(__file__), "temp", (conf.db_name[0] + ".db"))
            self.client = MilvusClient(db_file)
        else:
            self.client = MilvusClient(
                uri = conf.url,
                user = conf.user,
                password = conf.password,
                db_name = conf.db_name,
                token = conf.token,
                timeout = conf.timeout,
            )
        elapsed = round(time.perf_counter() - begin, 2)
        logger.info(f"init MilvusOperator success. Elapsed: {elapsed}s")


    def create_collection(self, collection_name: str):
        if self.client.has_collection(collection_name=collection_name):
            raise RuntimeError(f"collection: {collection_name} is already exists, please drop it firstly")
        else:
            begin = time.perf_counter()
            self.client.create_collection(
                collection_name=collection_name,
                dimension=768,  # The vectors we will use in this demo has 768 dimensions
            )
            elapsed = round(time.perf_counter() - begin, 2)
            logger.info(f"Create collection: \"{collection_name}\" success. Elapsed: {elapsed}s")


    def drop_collection(self, collection_name: str):
        if self.client.has_collection(collection_name=collection_name):
            begin = time.perf_counter()
            self.client.drop_collection(collection_name=collection_name)
            elapsed = round(time.perf_counter() - begin, 2)
            logger.info(f"Drop collection: \"{collection_name}\" success. Elapsed: {elapsed}s")
        else:
            logger.info(f"Ignore to drop collection: {collection_name} as it's not exists")


    def insert_documents(self, collection_name: str, data: list):
        if self.client.has_collection(collection_name=collection_name):
            result = self.client.insert(collection_name=collection_name, data=data)
            logger.info(f"Insert documents into \"{collection_name}\" success. {result}")
        else:
            # Bad Implementation
            logger.info(f"collection: {collection_name} is not exists! create it now")
            self.create_collection(collection_name)
            self.insert_documents(collection_name, data)


    def search_documents(self, collection_name: str, query_vectors: list):
        if self.client.has_collection(collection_name=collection_name):
            begin = time.perf_counter()
            try:
              return self.client.search(
                collection_name=collection_name,  # target collection
                data=query_vectors,  # query vectors
                limit=10,  # number of returned entities
                output_fields=["text", "subject"],  # specifies fields to be returned
              )
            finally:
              elapsed = round(time.perf_counter() - begin, 2)
              logger.info(f"Search documents from \"{collection_name}\" success. Elapsed: {elapsed}s")
        else:
            raise RuntimeError(f"collection: {collection_name} is not exists, please create it firstly")


#Our sentences we like to encode
docs = [
    '* Moka 此文本嵌入模型由 MokaAI 训练并开源，训练脚本使用 uniem',
    '* Massive 此文本嵌入模型通过**千万级**的中文句对数据集进行训练',
    '* Mixed 此文本嵌入模型支持中英双语的同质文本相似度计算，异质文本检索等功能，未来还会支持代码检索，ALL in one'
]

# Main
if __name__ == "__main__":
    milvus_operator = MilvusOperator(Configuration(True))
    milvus_operator.drop_collection("ai4p")
    milvus_operator.create_collection("ai4p")

    # doc_vectors = PyMilvusEmbedding().embedding_documents(docs)
    doc_vectors = M3eBaseEmbedding().embedding_documents(docs)
    milvus_operator.insert_documents("ai4p", doc_vectors)

    # search_vectors = PyMilvusEmbedding().embedding_query("人工智能")
    search_vectors = M3eBaseEmbedding().embedding_query("人工智能")
    related_docs = milvus_operator.search_documents("ai4p", search_vectors)

    # Return type of related_docs is SearchResult
    for related_doc in related_docs:
        if type(related_doc) == str:
            logger.info(f"{related_doc}")
        else:
            for sub_related_doc in related_doc:
                logger.info(f"{sub_related_doc}")