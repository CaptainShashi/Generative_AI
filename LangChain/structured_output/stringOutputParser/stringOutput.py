from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import TypedDict

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    type="text-generation"
)

model = ChatHuggingFace(llm=llm)

# First prompt: detailed report on a topic
template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=['topic']
)

# Second prompt: detailed summary
template2 = PromptTemplate(
    template="write a detailed summary of the following text:\n{text}",
    input_variables=['text']
)

# Define structured output schema
class Summary(TypedDict):
    summary: str

# Create structured model
structured_model = model.with_structured_output(Summary)

# Get detailed report (normal .content call)
prompt1 = template1.invoke({"topic": "black hole"})
response1 = model.invoke(prompt1)
print("Report:\n", response1.content)

# Use structured output for summary
prompt2 = template2.invoke({"text": response1.content})
response2 = structured_model.invoke(prompt2)
print("\nSummary:\n", response2['summary'])
