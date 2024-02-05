import pinecone
from langchain_community.vectorstores.pinecone import Pinecone

from app.backend.embeddings.openai_embeddings import embeddings
from app.backend.settings import settings

# TODO: Update pinecone-client to version >=3 (currently 2.2.4)
# Currently not working properly with serverless architecture
# See: https://www.reddit.com/r/LangChain/comments/199mklo/langchain_011_is_not_working_with_pineconeclient/
pinecone.init(
    api_key=settings.pinecone_api_key,
    environment=settings.pinecone_env_name
)

vector_store = Pinecone.from_existing_index(
    settings.pinecone_index_name, embeddings
)
