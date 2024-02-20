import uuid
from typing import Annotated

import bs4
from fastapi import Depends
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import GoogleDriveLoader, WebBaseLoader

from app.backend.chat.vector_stores.pgvector_vector_store import (
    build_vector_store_from_chatbot_id,
)
from app.backend.settings import Settings, get_settings


class DbService:
    def __init__(self, settings: Annotated[Settings, Depends(get_settings)]):
        self.settings = settings

    def sync_embeddings(self, chatbot_id: uuid.UUID) -> bool:
        self.vector_store = build_vector_store_from_chatbot_id(chatbot_id)
        # self.__clear_vector_store()
        # self.__add_documents_to_vector_store()
        self.testWebLoading()
        return True

    def testWebLoading(self):
        loader = WebBaseLoader(
            web_paths=[
                "https://www.piercingline.com/product/Titan-Ohrstecker-KREIS/TSO107-184989",
                "https://www.piercingline.com/product/Chirurgenstahl-Klemmkugel-KRISTALL/SLX800-93851",
            ],
            bs_kwargs=dict(
                parse_only=bs4.SoupStrainer(class_=("product-detail-description-text"))
            ),
        )
        docs = loader.load()  # TODO: Use loader.load_and_split() instead?
        print(docs)
        self.vector_store.add_documents(docs)

    def __clear_vector_store(self):
        self.vector_store.delete_collection()
        self.vector_store.create_collection()

    def __add_documents_to_vector_store(self):
        text_splitter = RecursiveCharacterTextSplitter(
            separators=[" ", ". ", "\n"], chunk_size=512, chunk_overlap=50
        )
        loader = GoogleDriveLoader(
            service_account_key="google-service-account-key.json",
            folder_id=self.settings.google_drive_vector_sources_folder_id,
            recursive=True,
            file_types=["document", "sheet", "pdf"],
        )
        docs = loader.load_and_split(text_splitter=text_splitter)
        self.vector_store.add_documents(docs)
