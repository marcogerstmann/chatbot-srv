from fastapi import APIRouter

from app.schemas.lead_request_schema import LeadRequestSchema
from app.services.leads_service import capture_lead

router = APIRouter(prefix="/leads")


@router.post("/")
def post_lead(request: LeadRequestSchema) -> bool:
    """Calculate solar potential"""

    capture_lead(request)
    return True
