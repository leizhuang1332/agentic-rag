from markitdown import MarkItDown

md = MarkItDown(docintel_endpoint="<document_intelligence_endpoint>")
result = md.convert("file:/Users/Ray/PycharmProjects/agentic-rag/data/阿里开发手册-泰山版.pdf")
print(result.text_content)