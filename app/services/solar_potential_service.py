from app.schemas.solar_potential_response_schema import SolarPotentialResponseSchema


def calculate_solar_potential(address: str) -> SolarPotentialResponseSchema:
    return SolarPotentialResponseSchema(
        roof_coverage_percent=42,
        panels_count=42,
        yearly_production_kwh=42,
        yearly_production_euro=42
    )
