from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4.0-turbo', temperature=0.7, max_completion_tokens=1000)
response = model.invoke("hello shashi")
print(response.content)


#max_completion_tokens :: used to produce response in the specified tokens 