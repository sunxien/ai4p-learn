# Connection to huggingface.co timed out
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# External Modules
from pymilvus import model
from pymilvus.model import DefaultEmbeddingFunction

# Current Project Modules
from pylang.logger import Logger

logger = Logger.get_root_logger()

class PyMilvusEmbedding:

    embedding_fn: DefaultEmbeddingFunction

    def __init__(self):
        self.embedding_fn = model.DefaultEmbeddingFunction(
            model_name = "GPTCache/paraphrase-albert-onnx",
            tokenizer_name = "GPTCache/paraphrase-albert-small-v2"
        )


    def embedding_documents(self, docs: list):
        vectors = self.embedding_fn.encode_documents(docs)
        logger.info(f"Dim: {self.embedding_fn.dim} {vectors[0].shape}")  # Dim: 768 (768,)

        data = [
            {"id": i, "vector": vectors[i], "text": docs[i], "subject": "history"} for i in range(len(vectors))
        ]
        logger.info(f"Data has {len(data)} entities, each with fields: {data[0].keys()}")

        first_vector = data[0]["vector"]
        logger.info(f"Vector dim: {len(first_vector)}")
        return data


    def embedding_query(self, query: str):
        return self.embedding_fn.encode_queries([query])



docs = [
    "Artificial intelligence was founded as an academic discipline in 1956.",
    "Alan Turing was the first person to conduct substantial research in AI.",
    "Born in Maida Vale, London, Turing was raised in southern England.",
]

# Main
if __name__ == "__main__":
    embedding = PyMilvusEmbedding()
    vector_list = embedding.embedding_documents(docs)

    # Print the embeddings
    for doc, vector in zip(docs, vector_list):
        logger.info(f"Doc: {doc}, Embedding: {vector}")
