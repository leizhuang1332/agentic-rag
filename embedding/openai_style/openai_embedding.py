from utils_d.common import get_vector_store


def embed_save(texts):
    batch_size = 64  # 匹配 OpenAI 接口限制
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]  # 拆分批次
        get_vector_store().add_texts(batch_texts)  # 逐批添加
        print(f"已完成第 {i // batch_size + 1} 批文本嵌入，共处理 {len(batch_texts)} 条")
    print(f"所有文本（共 {len(texts)} 条）已全部嵌入并保存到 Milvus")

def embed_query(text):
    # Use the vectorstore as a retriever
    retriever = get_vector_store().as_retriever()

    # Retrieve the most similar text
    retrieved_documents = retriever.invoke(text)

    # show the retrieved document's content
    return retrieved_documents

if __name__ == '__main__':
    embed_save("haha")
