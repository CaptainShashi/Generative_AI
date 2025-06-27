from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatOpenAI()

prompts=PromptTemplate(
    template="give me example of 5 {topic}",
    input_types=['topic']
)

parser=StrOutputParser()

chain=prompts | model | parser    # ( prompts-->model--->parser)  "|" this symbol used to connect input to model then to output

result=chain.invoke({"topic":"cricket"})

print(result)