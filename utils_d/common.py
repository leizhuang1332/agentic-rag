from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

import os

load_dotenv(override=True)

ZHIPUAI_API_KEY = os.getenv("ZHIPUAI_API_KEY")
ZHIPUAI_EMBEDDING = os.getenv("ZHIPUAI_EMBEDDING")
ZHIPUAI_BASE_URL = os.getenv("ZHIPUAI_BASE_URL")

embeddings = OpenAIEmbeddings(
    api_key=ZHIPUAI_API_KEY,
    model=ZHIPUAI_EMBEDDING,
    base_url=ZHIPUAI_BASE_URL,
    dimensions=256
)


def get_embedding():
    return embeddings


from pathlib import Path
from langchain_milvus import Milvus

vector_store_dir = Path(__file__).parent.parent.parent / "vector_stores"
vector_store_dir.mkdir(exist_ok=True)

vector_store = Milvus(
    embedding_function=get_embedding(),
    connection_args={"uri": str(vector_store_dir / "milvus_example.db")},
    index_params={"index_type": "FLAT", "metric_type": "L2"},
)


def get_vector_store():
    return vector_store
