## role based prompt --> change the role of the model

from langchain_core.prompts import ChatPromptTemplate

chat_prompt=ChatPromptTemplate.from_template([
    {"system":"you are an experienced {profession}"},
    {"role":"tell me about {topic}"}
])

formatted_message=chat_prompt.format_messages(prfession="engineer", topic="thermodynamics")