from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
from langchain.schema.runnable import RunnableParallel    # used to run parallel execution
from dotenv import load_dotenv

load_dotenv()

# ptompt1
prompt1=PromptTemplate(
    template="can you give example for {text}",
    input_variables=['text']
)

# prompt2
prompt2=PromptTemplate(
    template="can you give example for {text}",
    input_variables=['text']
)

#prompt3
prompt3=PromptTemplate(
    template="can you give example for {text}",
    input_variables=['text']
)

model1=ChatOpenAI()
model2=ChatAnthropic()
parser=StrOutputParser()


# parallel chain completed 
parallel_chain=RunnableParallel(
    {
        "notes": prompt1 | model1 | parser ,        
        "quiz" : prompt2 | model2 | parser 
    }
)

merge_chain= prompt3 | model1 |parser

chain = parallel_chain | merge_chain

result=chain.invoke({"text":"text"})
print(result)

