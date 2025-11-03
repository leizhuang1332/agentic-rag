from langchain_community.document_loaders.parsers import RapidOCRBlobParser
from langchain_pymupdf4llm import PyMuPDF4LLMLoader


def get_document_page(file_path):
    loader = PyMuPDF4LLMLoader(
        file_path,
        mode="page",
        extract_images=True,
        images_parser=RapidOCRBlobParser()
    )
    docs = loader.load()
    pg_size = len(docs)
    for i in range(pg_size):
        yield docs[i].page_content

def get_document(file_path):
    pages = get_document_page(file_path)
    document = "".join(pages)
    return document


if __name__ == '__main__':
    text = get_document("../../data/阿里开发手册-泰山版.pdf")
    print(text)
