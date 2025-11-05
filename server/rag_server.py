from embedding.openai_style.openai_embedding import embed_save, embed_query
from extract.pymupdf4llm_langchain.file_pymupdf4llm_langchain import get_document
from splitter.markdown_splitter.md_splitter import split, split_chunk

if __name__ == '__main__':
    # document = get_document("../data/阿里开发手册-泰山版.pdf")
    # md = split(document)
    # chunks = split_chunk(md)
    # texts = [chunk.page_content for chunk in chunks]
    # embed_save(texts)

    for e in embed_query("java代码的命名风格是怎么样的？"):
        print(e)