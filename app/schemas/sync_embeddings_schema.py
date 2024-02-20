import uuid

from app.schemas.base_schema import BaseSchema


class SyncEmbeddingsSchema(BaseSchema):
    chatbot_id: uuid.UUID
