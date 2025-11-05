from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

from extract.pymupdf4llm_langchain.file_pymupdf4llm_langchain import get_document

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]


def split(markdown_document):
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on,
        # return_each_line=True,
    )
    return markdown_splitter.split_text(markdown_document)


def split_chunk(md_header_splits):
    chunk_size = 150
    chunk_overlap = 50
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    # Split
    splits = text_splitter.split_documents(md_header_splits)
    return splits


if __name__ == '__main__':
    document = get_document("../../data/阿里开发手册-泰山版.pdf")
    md = split(document)
    chunks = split_chunk(md)
    for chunk in chunks:
        print()
        print("-"*80)
        print()
        print(chunk.page_content)
