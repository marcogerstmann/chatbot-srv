from langchain_openai import OpenAIEmbeddings

from app.backend.settings import settings

embeddings = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)
