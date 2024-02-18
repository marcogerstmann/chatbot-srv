from langchain_community.vectorstores.pgvector import PGVector

from app.backend.chat.embeddings.openai_embeddings import embeddings
from app.backend.settings import get_settings

vector_store = PGVector(
    connection_string=get_settings().postgres_connection_string,
    collection_name="base",
    embedding_function=embeddings,
)
