from typing import Annotated

from fastapi import Depends

from app.backend.chat.agents.knowledge_base_agent import build_agent_executor
from app.repositories.chatbot_repository import ChatbotRepository


class ChatService:
    def __init__(
        self,
        chatbot_repository: Annotated[ChatbotRepository, Depends(ChatbotRepository)],
    ):
        self.chatbot_repository = chatbot_repository

    def handle_knowledge_base_message(
        self, chatbot_id: str, session_id: str, question: str
    ) -> str:
        chatbot = self.chatbot_repository.get(chatbot_id)
        agent_executor = build_agent_executor(
            session_id=session_id, system_prompt=chatbot.system_prompt
        )
        result = agent_executor.invoke({"input": question})
        return result["output"]
