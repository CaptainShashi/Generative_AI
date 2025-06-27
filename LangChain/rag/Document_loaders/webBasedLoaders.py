from langchain.document_loaders import WebBaseLoader

url='https://www.linkedin.com/'  # enter website you want to extract 

loader=WebBaseLoader(url)

docs=loader.load()

print(docs.content)