from langchain_openai import ChatOpenAI
from langchain_core .prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# prompt 1
prompt1=PromptTemplate(
    template="can you give info  about {topivc}",
    input_types=['topic']
)

# prompt2

prompt2=PromptTemplate(
    template="can you give into about {topic}",
    input_types=['topic']
)

model=ChatOpenAI()
parser=StrOutputParser()

chain=prompt1 | model | parser | prompt2 | model | parser 

result=chain.invoke({"topic":"fruits"})
print(result)
