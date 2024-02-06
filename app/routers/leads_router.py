from fastapi import APIRouter

from app.schemas.lead_request_schema import LeadRequestSchema
from app.services.leads_service import capture_lead

router = APIRouter(prefix="/leads")


@router.post("", response_model=bool)
def post_lead(request: LeadRequestSchema) -> bool:
    """Capture a lead"""

    return capture_lead(request)
