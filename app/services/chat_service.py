import uuid
from typing import Annotated

from fastapi import Depends
from langchain.agents import AgentExecutor, create_openai_functions_agent, tool
from langchain.chains import ConversationalRetrievalChain
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
from app.repositories.chatbot_repository import ChatbotRepository


class ChatService:
    def __init__(
        self,
        chatbot_repository: Annotated[ChatbotRepository, Depends(ChatbotRepository)],
    ):
        self.chatbot_repository = chatbot_repository

    # TODO: Can be deleted
    def handle_knowledge_base_message(
        self, chatbot_id: uuid.UUID, session_id: str, question: str
    ) -> str:
        vector_store = build_vector_store_from_chatbot_id(chatbot_id)
        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vector_store.as_retriever(),
            memory=build_memory(session_id),
            verbose=True,
        )
        result = chain.invoke({"question": question})
        return result["answer"]

    @tool
    def retriever_tool(query: str):
        """Get relevant documents from the knowledge base. Always look here if you can find the answer to the users question."""
        # TODO: Build retriever dynamically based on chatbot id
        retriever = build_vector_store_from_chatbot_id(CHATBOT_AVA_ID).as_retriever()
        docs = retriever.get_relevant_documents(query)
        return docs

    @tool
    def no_answer_tool() -> str:
        """Run this if you don't know the answer to the users question."""
        # TODO: Should offer contact to a human via the Voiceflow runtime
        return "Das weiß ich leider nicht."

    def handle_knowledge_base_message_as_agent(
        self, chatbot_id: str, session_id: str, question: str
    ) -> str:
        agent_executor = self.__build_agent_executor(chatbot_id, session_id)
        result = agent_executor.invoke({"input": question})
        return result["output"]

    def __build_agent_executor(self, chatbot_id: str, session_id: str) -> AgentExecutor:
        chatbot = self.chatbot_repository.get(chatbot_id)
        tools = [self.retriever_tool, self.no_answer_tool]
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(chatbot.system_prompt),
                HumanMessagePromptTemplate.from_template("{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )
        agent = create_openai_functions_agent(llm=llm, prompt=prompt, tools=tools)
        agent.bind
        return AgentExecutor(
            agent=agent, tools=tools, memory=build_memory(session_id), verbose=True
        )
