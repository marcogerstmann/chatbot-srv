import uuid

from langchain.chains import ConversationalRetrievalChain

from app.backend.chat.llms.chatopenai import llm
from app.backend.chat.memories.postgres_memory import build_memory
from app.backend.chat.vector_stores.pgvector_vector_store import (
    build_vector_store_from_chatbot_id,
)


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
