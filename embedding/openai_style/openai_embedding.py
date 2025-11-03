import os

from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

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

if __name__ == '__main__':
    query = embeddings.embed_query("哈哈哈")
    print(query)
