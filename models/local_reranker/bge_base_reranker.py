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
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from langchain_community.vectorstores import Milvus, FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder

# Current Project Modules
from pylang.logger import logger
logger = Logger.get_root_logger()

class BgeBaseReranker:

    embeddingsModel: HuggingFaceEmbeddings
    tokenizer: AutoTokenizer
    classification: AutoModelForSequenceClassification

    def __init__(self, embedding_model_name: str, reranker_model_name: str):
        self.embeddingsModel = HuggingFaceEmbeddings(model_name=embedding_model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(reranker_model_name)
        self.classification = AutoModelForSequenceClassification.from_pretrained(reranker_model_name)
        self.classification.eval()
        self.classification.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

    # FIXME run error here
    def reranking_contents(self, query: str, docs: list):
        inputs = self.tokenizer([query] * len(docs), [doc for doc in docs])
        scores = self.classification(**inputs).logits.softmax(dim=-1)[:, 1].tolist()
        reranking_docs = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in reranking_docs]


    # FIXME run error here
    def reranking_documents(self, query: str, docs: list):
        inputs = self.tokenizer([query] * len(docs), [doc.page_content for doc in docs])
        scores = self.classification(**inputs).logits.softmax(dim=-1)[:, 1].tolist()
        reranking_docs = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in reranking_docs]

#
query='what is a panda?'

docs = [
    'The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear',
    "Paris is in France."
]

# Main
if __name__ == "__main__":

    from modelscope import snapshot_download
    embedding_model_name = snapshot_download("AI-ModelScope/m3e-base", revision='master')

    reranker_model_name = "BAAI/bge-reranker-base"

    reranker = BgeBaseReranker(embedding_model_name, reranker_model_name)
    reranked_docs = reranker.reranking_contents(query, docs)
