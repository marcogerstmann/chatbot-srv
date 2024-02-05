from app.schemas.solar_potential_response_schema import SolarPotentialResponseSchema
from app.services.google_api_service import get_coordinates, get_solar_building_insights


def calculate_solar_potential(address: str) -> SolarPotentialResponseSchema:
    coordinates = get_coordinates(address)
    building_insights = get_solar_building_insights(coordinates)

    # TODO: Finish implementation of solar potentail calculation
    return SolarPotentialResponseSchema(
        roof_coverage_percent=42,
        panels_count=42,
        yearly_production_kwh=42,
        yearly_production_euro=42
    )
