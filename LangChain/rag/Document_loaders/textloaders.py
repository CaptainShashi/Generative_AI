import os
from langchain_community.document_loaders import TextLoader

file_path = os.path.join("..", "intro.txt")  # assumes one level up from current dir
loader = TextLoader(file_path, encoding='utf-8')
docs = loader.load()
print(docs)


# we can pass this document ot LLM and aksqueries from that docs 
