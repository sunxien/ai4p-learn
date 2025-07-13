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

# Connection to huggingface.co timed out
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

import asyncio

# External Modules
from infinity_emb import AsyncEmbeddingEngine, EngineArgs

# Current Project Modules
from pylang.logger import Logger
logger = Logger.get_root_logger()

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

    # def reranking_documents(self, query: str, docs: list):
    #     with self.engine:
    #         ranking, usage = self.engine.rerank(query=query, docs=docs)
    #         print(list(zip(ranking, docs)))


    async def reranking_documents(self, query: str, docs: list):
        with self.engine:
            ranking, usage = await self.engine.rerank(query=query, docs=docs)
            ranking_docs = list(zip(ranking, docs))
            for ranking_doc in ranking_docs:
                # RerankReturnRerankReturnType(relevance_score=3.7410045e-05, document='Paris is in France.', index=1),
                # 'Paris is in France.'Type
                logger.info(f"{ranking_doc}")


#
query='what is a panda?'

docs = [
    'The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear',
    "Paris is in France."
]

# Main
if __name__ == "__main__":
    reranker = BgeBaseReranker()
    asyncio.run(reranker.reranking_documents(query, docs))
