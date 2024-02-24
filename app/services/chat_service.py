import uuid

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
from app.prompts import AVA_SYSTEM_PROMPT


class ChatService:
    def __init__(self):
        pass

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
        retriever = build_vector_store_from_chatbot_id(
            CHATBOT_AVA_ID
        ).as_retriever()  # TODO: Build retriever dynamically based on chatbot id
        docs = retriever.get_relevant_documents(query)
        return docs

    @tool
    def no_answer_tool() -> str:
        """Run this if you don't know the answer to the users question."""
        # TODO: Should offer contact to a human via the Voiceflow runtime
        return "Das weiß ich leider nicht."

    def handle_knowledge_base_message_as_agent(
        self, chatbot_id: uuid.UUID, session_id: str, question: str
    ) -> str:
        agent_executor = self.build_agent_executor(session_id)
        result = agent_executor.invoke({"input": question})
        print(result)
        return result["output"]

    def build_agent_executor(self, session_id: str) -> AgentExecutor:
        tools = [self.retriever_tool, self.no_answer_tool]
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(AVA_SYSTEM_PROMPT),
                HumanMessagePromptTemplate.from_template("{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )
        agent = create_openai_functions_agent(llm=llm, prompt=prompt, tools=tools)
        agent.bind
        return AgentExecutor(
            agent=agent, tools=tools, memory=build_memory(session_id), verbose=True
        )
