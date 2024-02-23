from langchain_openai import ChatOpenAI

from app.backend.settings import get_settings

llm = ChatOpenAI(openai_api_key=get_settings().openai_api_key)
