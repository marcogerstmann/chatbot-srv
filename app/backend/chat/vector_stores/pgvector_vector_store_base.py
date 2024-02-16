from langchain_community.vectorstores.pgvector import PGVector

from app.backend.chat.embeddings.openai_embeddings import embeddings
from app.backend.config import config

vector_store = PGVector(
    connection_string=config.postgres_connection_string,
    collection_name="base",
    embedding_function=embeddings,
)
