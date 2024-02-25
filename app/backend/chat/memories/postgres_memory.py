from langchain.memory import ConversationBufferWindowMemory, PostgresChatMessageHistory

from app.backend.settings import get_settings


def build_memory(session_id: str):
    return ConversationBufferWindowMemory(
        chat_memory=PostgresChatMessageHistory(
            connection_string=get_settings().postgres_connection_string,
            session_id=session_id,
        ),
        k=5,
        return_messages=True,
    )
