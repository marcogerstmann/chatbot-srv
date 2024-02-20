import uuid

from langchain.chains import ConversationChain, RetrievalQA

from app.backend.chat.llms.chatopenai import chat
from app.backend.chat.memories.postgres_memory import build_memory
from app.backend.chat.vector_stores.pgvector_vector_store import (
    build_vector_store_from_chatbot_id,
)


class ChatService:
    def __init__(self):
        pass

    def handle_conversation_prompt(self, prompt: str, session_id: str) -> str:
        chain = ConversationChain(
            llm=chat, verbose=True, memory=build_memory(session_id)
        )
        return chain.predict(input=prompt)

    def handle_faq_question(self, chatbot_id: uuid.UUID, question: str) -> str:
        # TODO: Use ConversationalRetrievalChain instead of RetrievalQA to have memory
        vector_store = build_vector_store_from_chatbot_id(chatbot_id)
        chain = RetrievalQA.from_chain_type(
            llm=chat, retriever=vector_store.as_retriever(), chain_type="stuff"
        )
        output = chain.invoke({"query": question})
        return output["result"]
