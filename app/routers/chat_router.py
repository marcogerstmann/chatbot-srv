from typing import Annotated

from fastapi import APIRouter, Depends, Header

from app.schemas.chat_request_schema import ChatRequestSchema
from app.schemas.chat_response_schema import ChatResponseSchema
from app.services.chat_service import ChatService

router = APIRouter(prefix="/chat")


@router.post("", response_model=ChatResponseSchema)
def simple_chat(
    request: ChatRequestSchema,
    x_session_id: Annotated[str, Header()],
    chat_service: Annotated[ChatService, Depends(ChatService)],
) -> ChatResponseSchema:
    """Handle conversation prompt"""

    answer = chat_service.handle_conversation_prompt(request.input, x_session_id)
    return ChatResponseSchema(output=answer)


@router.post("/faq", response_model=ChatResponseSchema)
def faq_question(
    request: ChatRequestSchema,
    chat_service: Annotated[ChatService, Depends(ChatService)],
) -> ChatResponseSchema:
    """Handle FAQ chat message"""

    answer = chat_service.handle_faq_question(request.input)
    return ChatResponseSchema(output=answer)
