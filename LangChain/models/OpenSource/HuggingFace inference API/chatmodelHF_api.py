from langchain_community.chat_models import ChatHuggingFace  # For chat models
from langchain_huggingface import HuggingFaceEndpoint        # For using hosted Hugging Face endpoints
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# go to huggingFace-->profile--->Access token

llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # repo of model
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),  # API token stored in .env
    task="text-generation"  # task you want to perform
)

model = ChatHuggingFace(llm=llm)  # llm is prepared above and passed here 

result = model.invoke("what is the capital of india")

print(result.content)
