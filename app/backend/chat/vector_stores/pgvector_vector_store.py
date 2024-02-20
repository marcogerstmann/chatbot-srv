import uuid

from langchain_community.vectorstores.pgvector import PGVector

from app.backend.chat.embeddings.openai_embeddings import embeddings
from app.backend.settings import get_settings


def build_vector_store_from_chatbot_id(chatbot_id: uuid.UUID) -> PGVector:
    return build_vector_store(f"chatbot_{str(chatbot_id)}")


def build_vector_store(collection_name: str) -> PGVector:
    return PGVector(
        connection_string=get_settings().postgres_connection_string,
        collection_name=collection_name,
        embedding_function=embeddings,
    )
