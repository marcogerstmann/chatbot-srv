import uuid

from langchain.chains import ConversationalRetrievalChain

from app.backend.chat.llms.chatopenai import llm
from app.backend.chat.vector_stores.pgvector_vector_store import (
    build_vector_store_from_chatbot_id,
)


class ChatService:
    def __init__(self):
        pass

    def handle_faq_question(
        self, chatbot_id: uuid.UUID, session_id: str, question: str
    ) -> str:
        vector_store = build_vector_store_from_chatbot_id(chatbot_id)
        # TODO: Add memory and chat_history
        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            # memory=build_memory(session_id),
            retriever=vector_store.as_retriever(),
            verbose=True,
        )
        result = chain.invoke({"question": question, "chat_history": []})
        return result["answer"]
