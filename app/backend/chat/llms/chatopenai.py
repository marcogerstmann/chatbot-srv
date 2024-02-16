from langchain_openai import ChatOpenAI

from app.backend.config import config

chat = ChatOpenAI(openai_api_key=config.openai_api_key)
