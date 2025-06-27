import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama     ## all 3rd party integration we always have langchain_community
import streamlit as st



load_dotenv()

os.environ['OPEN_API_KEY']=os.getenv("OPEN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]=True
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


# propt template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant, please respond to user queries."),
        ("user","Questions:{question}")
    ]
)

# streamlit framework

st.title("LangChain with ollama")
input_text = st.text_input("Please enter your input:")

#Ollama llms

llms=ollama(model='llama2')
output_parser=StrOutputParser()
chain=prompt|llms|output_parser

# to run the model we have to do [ olama run model_name  ex:: ollama run llama2]

if input_text:
     response=chain.invole({"question":input_text})
     st.write(response)