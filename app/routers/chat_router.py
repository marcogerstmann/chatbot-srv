import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, Header

from app.schemas.chat_request_schema import ChatRequestSchema
from app.schemas.chat_response_schema import ChatResponseSchema
from app.services.chat_service import ChatService

router = APIRouter(prefix="/chat")


@router.post("/knowledge-base", response_model=ChatResponseSchema)
def handle_knowledge_base_message(
    request: ChatRequestSchema,
    x_chatbot_id: Annotated[uuid.UUID, Header()],
    x_session_id: Annotated[str, Header()],
    chat_service: Annotated[ChatService, Depends(ChatService)],
) -> ChatResponseSchema:
    """Handle a knowledge base chat message"""

    answer = chat_service.handle_knowledge_base_message(
        x_chatbot_id, x_session_id, request.input
    )
    return ChatResponseSchema(output=answer)
