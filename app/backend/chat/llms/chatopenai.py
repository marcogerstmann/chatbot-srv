from langchain_openai import ChatOpenAI

from app.backend.settings import get_settings

llm = ChatOpenAI(
    openai_api_key=get_settings().openai_api_key,
    temperature=0.7,
    # model="gpt-3.5-turbo-0125",
    model="gpt-4-0125-preview",
)
