from app.schemas.base_schema import BaseSchema


class SolarPotentialResponseSchema(BaseSchema):
    roof_coverage_percent: int
    panels_count: int
    yearly_production_kwh: int
    yearly_production_euro: int
