from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

from app.backend.chat.agents.tools.get_context_tool import GetContextTool
from app.backend.chat.agents.tools.no_answer_tool import NoAnswerTool
from app.backend.chat.llms.chatopenai import llm
from app.backend.chat.memories.postgres_memory import build_memory
from app.backend.chat.vector_stores.pgvector_vector_store import (
    build_vector_store_from_chatbot_id,
)
from app.backend.db.models import Chatbot


def build_agent_executor(chatbot: Chatbot, session_id: str):
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(chatbot.system_prompt),
            HumanMessagePromptTemplate.from_template("{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    retriever = build_vector_store_from_chatbot_id(chatbot.id).as_retriever()
    tools = [GetContextTool(retriever), NoAnswerTool()]
    agent = create_openai_functions_agent(llm=llm, prompt=prompt, tools=tools)
    return AgentExecutor(
        agent=agent, tools=tools, memory=build_memory(session_id), verbose=True
    )
