from langchain_openai import OpenAIEmbeddings

from app.backend.settings import get_settings

embeddings = OpenAIEmbeddings(openai_api_key=get_settings().openai_api_key)
