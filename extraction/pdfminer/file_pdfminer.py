# 统计总页数
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

pdf_path = "/Users/Ray/PycharmProjects/agentic-rag/data/阿里开发手册-泰山版.pdf"

markdown_content = []

with open(pdf_path, 'rb') as fp:
    total_pages = len(list(PDFPage.get_pages(fp)))
    print(total_pages)

page_num = 0

for page_layout in extract_pages(pdf_path, laparams=LAParams()):
    page_num += 1
    print(f"处理第 {page_num}/{total_pages} 页")
    with open(pdf_path, 'rb') as fp:
        text = extract_text(fp, page_numbers=[page_num - 1])
        if text:
            markdown_content.append(text)

print(markdown_content)