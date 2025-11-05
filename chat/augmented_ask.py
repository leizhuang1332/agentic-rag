from chat.model_ds import getModel
from utils_d.common import get_vector_store


def build_rag_prompt(query, retrieved_docs):
    """
    构建RAG提示词
    """
    # 1. 拼接检索到的文档内容
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    # 2. 构建提示词模板
    prompt = f"""请根据以下上下文信息回答问题。如果上下文中有答案，请基于上下文回答；如果没有，请说明。

        上下文信息：
        {context}

        问题：{query}

        请给出详细、准确的回答：
    """
    return prompt

def call_llm_with_rag(query, vectorstore, llm_model):
    """
    完整的RAG流程：检索 + 提示词构建 + 调用大模型
    """
    # 1. 检索相关文档
    retrieved_docs = vectorstore.similarity_search(query, k=3)

    # 2. 构建提示词
    prompt = build_rag_prompt(query, retrieved_docs)

    # 3. 调用大模型
    response = llm_model.invoke(prompt)

    return response.content


if __name__ == '__main__':
    # 使用示例
    query = "java代码的命名风格是怎么样的？"
    result = call_llm_with_rag(query, get_vector_store(), getModel())
    print("用户提问：" + query)
    print("模型最终回答：" + result)