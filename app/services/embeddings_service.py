from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import GoogleDriveLoader

from app.backend.settings import settings
from app.backend.vector_stores.pgvector_vector_store_base import vector_store_base


def sync_embeddings() -> bool:
    clear_vector_store()
    add_documents_to_vector_store()
    return True


def clear_vector_store():
    vector_store_base.delete_collection()
    vector_store_base.create_collection()


def add_documents_to_vector_store():
    text_splitter = RecursiveCharacterTextSplitter(
        separators=[" ", ". ", "\n"], chunk_size=512, chunk_overlap=50
    )
    loader = GoogleDriveLoader(
        service_account_key="google-service-account-key.json",
        folder_id=settings.google_drive_base_vector_sources_folder_id,
        recursive=True,
        file_types=["document", "sheet", "pdf"],
    )
    docs = loader.load_and_split(text_splitter=text_splitter)
    vector_store_base.add_documents(docs)
