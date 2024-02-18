from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import GoogleDriveLoader
from sqlalchemy import create_engine

from app.backend.chat.vector_stores.pgvector_vector_store_base import vector_store
from app.backend.config import config
from app.backend.db.models.base import Base


class DbService:
    def __init__(self):
        pass

    def sync_embeddings(self) -> bool:
        self.__clear_vector_store()
        self.__add_documents_to_vector_store()
        return True

    def __clear_vector_store(self):
        vector_store.delete_collection()
        vector_store.create_collection()

    def __add_documents_to_vector_store(self):
        text_splitter = RecursiveCharacterTextSplitter(
            separators=[" ", ". ", "\n"], chunk_size=512, chunk_overlap=50
        )
        loader = GoogleDriveLoader(
            service_account_key="google-service-account-key.json",
            folder_id=config.google_drive_vector_sources_folder_id,
            recursive=True,
            file_types=["document", "sheet", "pdf"],
        )
        docs = loader.load_and_split(text_splitter=text_splitter)
        vector_store.add_documents(docs)
