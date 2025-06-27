from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model='gpt-4.0-turbo',temperature=0.8)

result=llm.invoke('hello chatgpt! how are you')

print(result)