from app.schemas.base_schema import BaseSchema


class SolarPotentialResponseSchema(BaseSchema):
    max_solar_panels_percentage: int
    panels_count: int
    yearly_production_kwh: float
    yearly_production_euro: float
