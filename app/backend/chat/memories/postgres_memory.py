from langchain.memory import ConversationBufferMemory, PostgresChatMessageHistory

from app.backend.config import config


def build_memory(session_id: str):
    return ConversationBufferMemory(
        chat_memory=PostgresChatMessageHistory(
            connection_string=config.postgres_connection_string, session_id=session_id
        )
    )
