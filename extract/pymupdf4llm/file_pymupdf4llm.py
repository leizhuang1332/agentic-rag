import pymupdf4llm

pdf_path = "/Users/Ray/PycharmProjects/agentic-rag/data/阿里开发手册-泰山版.pdf"

md_text = pymupdf4llm.to_markdown(pdf_path)

import pathlib

pathlib.Path("output.md").write_bytes(md_text.encode())

def extract_pdf(pdf_path):
    return pymupdf4llm.to_markdown(pdf_path)




