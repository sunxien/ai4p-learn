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
import os

from pylang.utils.utils import *

content = '''Handling non-uniform document lengths: Real-world document collections often contain texts of varying sizes. Splitting ensures consistent processing across all documents.\n
    Overcoming model limitations: Many embedding models and language models have maximum input size constraints. Splitting allows us to process documents that would otherwise exceed these limits.\n
    Improving representation quality: For longer documents, the quality of embeddings or other representations may degrade as they try to capture too much information. Splitting can lead to more focused and accurate representations of each section.\n
    Enhancing retrieval precision: In information retrieval systems, splitting can improve the granularity of search results, allowing for more precise matching of queries to relevant document sections.\n
    Optimizing computational resources: Working with smaller chunks of text can be more memory-efficient and allow for better parallelization of processing tasks.'''



documents = [
    "Handling non-uniform document lengths: Real-world document collections often contain texts of varying sizes. Splitting ensures consistent processing across all documents.",
    "Overcoming model limitations: Many embedding models and language models have maximum input size constraints. Splitting allows us to process documents that would otherwise exceed these limits.",
    "Improving representation quality: For longer documents, the quality of embeddings or other representations may degrade as they try to capture too much information. Splitting can lead to more focused and accurate representations of each section.",
    "Enhancing retrieval precision: In information retrieval systems, splitting can improve the granularity of search results, allowing for more precise matching of queries to relevant document sections.",
    "Optimizing computational resources: Working with smaller chunks of text can be more memory-efficient and allow for better parallelization of processing tasks.",
]


CITY_CODE_JSON_FILE = join_paths(filedir(__file__),"citycode-2019-08-23.json")

def get_city_code(city_name: str):
    if not city_name or city_name == "":
        raise RuntimeError(f"city name: {city_name} is invalid")

    if os.path.exists(CITY_CODE_JSON_FILE):
        import json
        with open(CITY_CODE_JSON_FILE, 'r', encoding='utf-8') as jf:
            json_array = json.load(jf)
            # print(type(json_array))
            for json_elem in json_array:
                # print(type(json_elem))
                # print(json_elem['city_name'], json_elem['city_code'])
                if json_elem['city_name'] == city_name:
                    return json_elem['city_code']
    else:
        raise RuntimeError(f"{CITY_CODE_JSON_FILE} is not found")