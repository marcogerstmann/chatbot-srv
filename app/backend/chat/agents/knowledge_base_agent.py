from langchain.agents import AgentExecutor, create_openai_functions_agent, tool
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

from app.backend.chat.llms.chatopenai import llm
from app.backend.chat.memories.postgres_memory import build_memory
from app.backend.chat.vector_stores.pgvector_vector_store import (
    build_vector_store_from_chatbot_id,
)
from app.constants import CHATBOT_AVA_ID


# TODO: Should build the retriever based on a chatbot_id passed as a function parameter
@tool
def get_context_to_answer_user_question_tool(query: str):
    """ALWAYS get the relevant context from this database before answering the users question."""
    retriever = build_vector_store_from_chatbot_id(CHATBOT_AVA_ID).as_retriever()
    docs = retriever.get_relevant_documents(query)
    return docs


@tool
def no_answer_tool() -> str:
    """Run this if you don't know the answer to the users question."""
    # TODO: Should offer contact to a human via the Voiceflow runtime
    return "Das weiß ich leider nicht."


def build_agent_executor(session_id: str, system_prompt: str):
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(system_prompt),
            HumanMessagePromptTemplate.from_template("{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    tools = [get_context_to_answer_user_question_tool, no_answer_tool]
    agent = create_openai_functions_agent(llm=llm, prompt=prompt, tools=tools)
    return AgentExecutor(
        agent=agent, tools=tools, memory=build_memory(session_id), verbose=True
    )
