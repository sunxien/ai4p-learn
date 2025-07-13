# Connection to huggingface.co timed out
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

import asyncio

# External Modules
from infinity_emb import AsyncEmbeddingEngine, EngineArgs

# Current Project Modules
from pylang.logger import Logger

class BgeBaseReranker:

    engine: AsyncEmbeddingEngine

    def __init__(self):
        self.engine = AsyncEmbeddingEngine.from_args(
            EngineArgs(
                model_name_or_path="BAAI/bge-reranker-base",
                device="cpu",
                engine="torch"
                # or engine="optimum" for onnx
            )
        )


    async def reranking(self, query: str, docs: list):
        async with self.engine:
            ranking, usage = await self.engine.rerank(query=query, docs=docs)
            print(list(zip(ranking, docs)))


#
query='what is a panda?'

docs = [
    'The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear',
    "Paris is in France."
]

if __name__ == "__main__":
    reranker = BgeBaseReranker()
    asyncio.run(reranker.reranking(query, docs))
    pass