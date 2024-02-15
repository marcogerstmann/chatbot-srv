from fastapi import APIRouter

from app.schemas.chat_request_schema import ChatRequestSchema
from app.schemas.chat_response_schema import ChatResponseSchema
from app.services.faq_service import answer_question, answer_simple_chat

router = APIRouter(prefix="/chat")


@router.post("", response_model=ChatResponseSchema)
def simple_chat(request: ChatRequestSchema) -> ChatResponseSchema:
    """Handle FAQ chat message"""

    answer = answer_simple_chat(request.input)
    return ChatResponseSchema(output=answer)


@router.post("/faq", response_model=ChatResponseSchema)
def handle_faq_chat_message(request: ChatRequestSchema) -> ChatResponseSchema:
    """Handle FAQ chat message"""

    answer = answer_question(request.input)
    return ChatResponseSchema(output=answer)
