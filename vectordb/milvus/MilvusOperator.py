# System Modules
import time

# External Modules
from pymilvus import MilvusClient

# Current Project Modules
from pylang.logger import Logger
from vectordb.milvus.Configuration import Configuration

logger = Logger.get_root_logger()

class MilvusOperator:

    client: MilvusClient

    def __init__(self, conf: Configuration):
        begin = time.perf_counter()
        if conf.local:
            db_file = "./temp/" + conf.db_name[0] + ".db"
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
        client = self.client
        if client.has_collection(collection_name=collection_name):
            client.drop_collection(collection_name=collection_name)
            logger.info(f"Drop collection: \"{collection_name}\" success")

        client.create_collection(
            collection_name=collection_name,
            dimension=768,  # The vectors we will use in this demo has 768 dimensions
        )
        logger.info(f"Create collection: \"{collection_name}\" success")


    def insert_documents(self, collection_name: str, data: list):
        client = self.client
        client.insert(collection_name=collection_name, data=data)
        logger.info(f"Insert documents into \"{collection_name}\" success")


    def search_documents(self, collection_name: str, query_vectors: list):
        client = self.client
        return client.search(
            collection_name=collection_name,  # target collection
            data=query_vectors,  # query vectors
            limit=10,  # number of returned entities
            output_fields=["text", "subject"],  # specifies fields to be returned
        )


if __name__ == "__main__":
    milvus_operator = MilvusOperator(Configuration(True))
    logger.info("milvus operator....")