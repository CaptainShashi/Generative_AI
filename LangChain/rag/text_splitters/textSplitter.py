from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Load the text file
loader = TextLoader('LANGCHAIN/RAG/intro.txt', encoding='utf-8')
docs = loader.load()

# Initialize the text splitter
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
)

# Split the documents
split_docs = text_splitter.split_documents(docs)

# Print the result
print(split_docs)
