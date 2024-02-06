from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

from app.backend.vector_stores.pinecone_vector_store import vector_store


def sync_embeddings() -> bool:
    clear_vector_store()
    add_file_to_vetor_store()
    return True


def clear_vector_store():
    vector_store.delete(delete_all=True)


def add_file_to_vetor_store():
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=200,
        chunk_overlap=0
    )
    loader = TextLoader("./temp/facts.txt")
    docs = loader.load_and_split(text_splitter=text_splitter)
    vector_store.add_documents(docs)
