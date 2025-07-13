
# External Modules
from sentence_transformers import SentenceTransformer

# Current Project Modules
from pylang.logger import Logger

logger = Logger.get_root_logger()

class M3eBaseEmbedding:

    transformer: SentenceTransformer

    def __init__(self):
        from modelscope import snapshot_download
        model_dir = snapshot_download("AI-ModelScope/m3e-base", revision='master')
        self.transformer = SentenceTransformer(model_dir)


    def embedding_documents(self, docs: list):
        #Sentences are encoded by calling model.encode()
        vectors = self.transformer.encode_document(docs)
        logger.info(f"Dim: {self.transformer.get_sentence_embedding_dimension()} {vectors[0].shape}")

        data = [
            {"id": i, "vector": vectors[i], "text": docs[i], "subject": "history"} for i in range(len(vectors))
        ]
        logger.info(f"Data has {len(data)} entities, each with fields: {data[0].keys()}")

        first_vector = data[0]["vector"]
        logger.info(f"Vector dim: {len(first_vector)}")
        return data


    def embedding_query(self, query: str):
        return self.transformer.encode_query([query])


# Our sentences we like to encode
docs = [
    '* Moka 此文本嵌入模型由 MokaAI 训练并开源，训练脚本使用 uniem',
    '* Massive 此文本嵌入模型通过**千万级**的中文句对数据集进行训练',
    '* Mixed 此文本嵌入模型支持中英双语的同质文本相似度计算，异质文本检索等功能，未来还会支持代码检索，ALL in one'
]

if __name__ == "__main__":

    embedding = M3eBaseEmbedding()
    vector_list = embedding.embedding_documents(docs)

    # Print the embeddings
    for doc, vector in zip(docs, vector_list):
        logger.info(f"Doc: {doc}, Embedding: {vector}")