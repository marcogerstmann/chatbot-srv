from app.schemas.base_schema import BaseSchema


class LeadRequestSchema(BaseSchema):
    name: str
    address: str
    phone: str
