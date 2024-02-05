from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

from app.backend.vector_stores.pinecone_vector_store import vector_store


def create_embeddings() -> bool:
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=200,
        chunk_overlap=0
    )

    loader = TextLoader("./temp/facts.txt")
    docs = loader.load_and_split(text_splitter=text_splitter)

    vector_store.delete(delete_all=True)
    vector_store.add_documents(docs)

    return True
