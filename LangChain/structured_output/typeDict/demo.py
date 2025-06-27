from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict
import os

load_dotenv()

# Define schema
class Review(TypedDict):
    summery: str
    sentiment: str

# Initialize the Gemini model with API key from .env
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-001",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.4,
)

# Structured output calling
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps 
that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(result)
