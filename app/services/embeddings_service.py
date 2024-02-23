import uuid
from typing import Annotated

import bs4
from fastapi import Depends
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import GoogleDriveLoader, WebBaseLoader
from langchain_community.vectorstores import VectorStore

from app.backend.chat.vector_stores.pgvector_vector_store import (
    build_vector_store_from_chatbot_id,
)
from app.backend.db.models import Chatbot
from app.backend.settings import Settings, get_settings
from app.constants import CHATBOT_AVA_ID
from app.repositories.chatbot_repository import ChatbotRepository


class EmbeddingsService:
    def __init__(
        self,
        settings: Annotated[Settings, Depends(get_settings)],
        chatbot_repository: Annotated[ChatbotRepository, Depends(ChatbotRepository)],
    ):
        self.settings = settings
        self.chatbot_repository = chatbot_repository

    def sync_embeddings(self, chatbot_id: uuid.UUID) -> bool:
        chatbot = self.chatbot_repository.get(chatbot_id)
        if chatbot:
            vector_store = build_vector_store_from_chatbot_id(chatbot_id)
            self.__clear_vector_store(vector_store)
            docs = self.__load_docs(chatbot)
            vector_store.add_documents(docs)
        else:
            # TODO: Handle error case
            print(f"Chatbot not found with id: {chatbot_id}")
        return True

    def __clear_vector_store(self, vector_store: VectorStore):
        vector_store.delete_collection()
        vector_store.create_collection()

    def __load_docs(self, chatbot: Chatbot):
        if chatbot.id == CHATBOT_AVA_ID:
            return self.__load_docs_ava()

        return self.__load_docs_web_scraping(chatbot)

    def __load_docs_web_scraping(self, chatbot: Chatbot):
        loader = WebBaseLoader(
            web_paths=(
                vecor_scrape_url.url for vecor_scrape_url in chatbot.vector_scrape_urls
            ),
            bs_kwargs=dict(
                parse_only=bs4.SoupStrainer(
                    class_=(chatbot.vector_product_description_html_class)
                )
            ),
        )
        return loader.load()  # TODO: Use loader.load_and_split() instead?

    def __load_docs_ava(self):
        text_splitter = RecursiveCharacterTextSplitter(
            separators=[" ", ". ", "\n"], chunk_size=512, chunk_overlap=50
        )
        loader = GoogleDriveLoader(
            service_account_key="google-service-account-key.json",
            folder_id=self.settings.google_drive_vector_sources_ava_folder_id,
            recursive=True,
            file_types=["document", "sheet", "pdf"],
        )
        return loader.load_and_split(text_splitter=text_splitter)
