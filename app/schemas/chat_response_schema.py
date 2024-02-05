from app.schemas.base_schema import BaseSchema


class ChatResponseSchema(BaseSchema):
    output: str
