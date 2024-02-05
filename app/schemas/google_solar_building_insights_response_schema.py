from app.schemas.base_schema import BaseSchema


class GoogleSolarPanelConfig(BaseSchema):
    panels_count: int
    yearly_energy_dc_kwh: float


class GoogleSolarPotentialSchema(BaseSchema):
    max_array_panels_count: int
    max_array_area_meters_2: float
    max_sunshine_hours_per_year: float
    solar_panel_configs: list[GoogleSolarPanelConfig]


class GoogleSolarBuildingInsightResponseSchema(BaseSchema):
    name: str
    solar_potential: GoogleSolarPotentialSchema
