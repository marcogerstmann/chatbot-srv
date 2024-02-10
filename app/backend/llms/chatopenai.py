from langchain_openai import ChatOpenAI

from app.backend.settings import settings

chat = ChatOpenAI(openai_api_key=settings.openai_api_key)
