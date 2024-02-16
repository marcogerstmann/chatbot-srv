from langchain_openai import OpenAIEmbeddings

from app.backend.config import config

embeddings = OpenAIEmbeddings(openai_api_key=config.openai_api_key)
