## used to load document from a pdf file and convert ecah page into a document object 
# limitations:
    # not great with scanned pdfs 

from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('file_name.pdf')

docs=loader.load()
print(docs)
