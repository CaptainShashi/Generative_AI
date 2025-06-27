## 1) dynamic and reusable prompt 

from langchain_core.prompts import PromptTemplate

prompts = PromptTemplate.from_template("summerise {topic} in {emotion} tone")
print(prompts.format(topic="cricket", emotion="fun"))

