from typing import Annotated

from fastapi import APIRouter, Header

from app.schemas.chat_request_schema import ChatRequestSchema
from app.schemas.chat_response_schema import ChatResponseSchema
from app.services.chat_service import handle_conversation_prompt, handle_faq_question

router = APIRouter(prefix="/chat")


@router.post("", response_model=ChatResponseSchema)
def simple_chat(
    request: ChatRequestSchema, x_session_id: Annotated[str, Header()]
) -> ChatResponseSchema:
    """Handle conversation prompt"""
    print(request)

    answer = handle_conversation_prompt(request.input, x_session_id)
    return ChatResponseSchema(output=answer)


@router.post("/faq", response_model=ChatResponseSchema)
def faq_question(request: ChatRequestSchema) -> ChatResponseSchema:
    """Handle FAQ chat message"""

    answer = handle_faq_question(request.input)
    return ChatResponseSchema(output=answer)
