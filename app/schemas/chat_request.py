from app.schemas.base import BaseSchema


class ChatRequestSchema(BaseSchema):
    input: str
