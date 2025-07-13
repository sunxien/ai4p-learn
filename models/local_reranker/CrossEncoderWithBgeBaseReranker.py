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

# Temporary Solution  (it will cause crash!!!)
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder

# Current Project Modules
from pylang.logger import Logger
logger = Logger.get_root_logger()

class CrossEncoderWithBgeReranker:

    embeddingsModel: HuggingFaceEmbeddings
    rerankerModel: HuggingFaceCrossEncoder
    retriever: ContextualCompressionRetriever

    def __init__(self, embedding_model_name: str, reranker_model_name: str):
        self.embeddingsModel = HuggingFaceEmbeddings(model_name=embedding_model_name)
        self.rerankerModel = HuggingFaceCrossEncoder(model_name=reranker_model_name)


    def reranking_contents(self, query: str, docs: list):
        return ContextualCompressionRetriever(
            base_compressor=CrossEncoderReranker(model=self.rerankerModel, top_n=3),
            base_retriever=FAISS.from_texts(docs, self.embeddingsModel).as_retriever(
                search_kwargs={"k": 10}
            )
        ).invoke(query)


    def reranking_documents(self, query: str, docs: list):
        return ContextualCompressionRetriever(
            base_compressor=CrossEncoderReranker(model=self.rerankerModel, top_n=3),
            base_retriever=FAISS.from_documents(docs, self.embeddingsModel).as_retriever(
                search_kwargs={"k": 10}
            )
        ).invoke(query)


#
query='what is a panda?'

docs = [
    'The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear',
    "Paris is in France."
]

# Main
if __name__ == "__main__":
    # ImportError: Could not import faiss python package.
    # Please install it with `pip install faiss-gpu` (for CUDA supported GPU)
    # or `pip install faiss-cpu` (depending on Python version).
    # embedding_model_name="sentence-transformers/msmarco-distilbert-dot-v5"

    from modelscope import snapshot_download
    embedding_model_name = snapshot_download("AI-ModelScope/m3e-base", revision='master')

    reranker_model_name="BAAI/bge-reranker-base"

    reranker = CrossEncoderWithBgeReranker(embedding_model_name, reranker_model_name)
    reranking_docs = reranker.reranking_contents(query, docs)

    # Document list
    for ranking_doc in reranking_docs:
        # RerankReturnRerankReturnType(relevance_score=3.7410045e-05, document='Paris is in France.', index=1),
        # 'Paris is in France.'Type
        logger.info(f"{ranking_doc}")
