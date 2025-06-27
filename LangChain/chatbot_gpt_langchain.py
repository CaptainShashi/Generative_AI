import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant, please respond to user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain with OpenAI")
input_text = st.text_input("Please enter your input:")

# OpenAI LLM
model_name = 'gpt-3.5-turbo'  #
llm = ChatOpenAI(model=model_name)
output_parser = StrOutputParser()

# LangChain pipeline
chain = prompt | llm | output_parser

# Response
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
