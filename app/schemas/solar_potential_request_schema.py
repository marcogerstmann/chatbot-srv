from app.schemas.base_schema import BaseSchema


class SolarPotentialRequestSchema(BaseSchema):
    address: str
    max_solar_panels_percentage: float = 100
