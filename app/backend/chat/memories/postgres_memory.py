from langchain.memory import ConversationBufferMemory, PostgresChatMessageHistory

from app.backend.settings import get_settings


def build_memory(session_id: str):
    return ConversationBufferMemory(
        chat_memory=PostgresChatMessageHistory(
            connection_string=get_settings().postgres_connection_string,
            session_id=session_id,
        ),
        return_messages=True,
    )
