from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatAnthropic(model="claude-3-opus-20240229", temperature=0.9)
response = model.invoke("hello shashi")
print(response.content)
