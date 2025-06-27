from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser
from langchain.embeddings import OpenAIEmbeddings


# load document
loaders=TextLoader('file_name.pdf')
document=loaders.load()

# split text in that documenyt into chunks 
split=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
text_splitter=split.split_text(document)

# store into vectors ( FAISS )
vector_store=FAISS.from_documents(text_splitter,OpenAIEmbeddings())

# create a retriever
retriever=vector_store.as_retriever()

# manually retrieve Relevent documents 
query="what are the key topics in the documents"
retrieved_docs=retriever._get_relevant_documents(query)

# combine retriever text into a single prompt
retrieved_text="\n".join([doc.page_content for doc in retrieved_docs])

# initialise the LLM
llm=openai(model="gpt-4.0-turbo",temperature=0.4)

# manually pass retrievedtext to llm
prompt=f"based  on the following text answer the following questions:{query}\n\n{retrieved_text}"  # f used to insert variables in prompt 
answer=llm.predict(prompt)
print(answer)