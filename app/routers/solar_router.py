from fastapi import APIRouter

from app.schemas.solar_potential_request_schema import SolarPotentialRequestSchema
from app.schemas.solar_potential_response_schema import SolarPotentialResponseSchema
from app.services.solar_potential_service import calculate_solar_potential

router = APIRouter(prefix="/solar")


@router.post("/potential", response_model=SolarPotentialResponseSchema)
def post_solar_potential(
    request: SolarPotentialRequestSchema,
) -> SolarPotentialResponseSchema:
    """Calculate solar potential"""

    return calculate_solar_potential(
        request.address, request.max_solar_panels_percentage
    )
