from app.schemas.base_schema import BaseSchema


class ChatRequestSchema(BaseSchema):
    input: str
