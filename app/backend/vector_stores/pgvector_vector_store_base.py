from langchain_community.vectorstores.pgvector import PGVector
from app.backend.settings import settings

from app.backend.embeddings.openai_embeddings import embeddings

vector_store_base = PGVector(
    connection_string=settings.postgres_connection_string,
    collection_name=settings.postgres_vector_base_collection_name,
    embedding_function=embeddings,
)
