from app.constants import LEADS_GOOGLE_SPREADSHEET_ID
from app.schemas.lead_request_schema import LeadRequestSchema
from app.services.google_api_service import capture_lead_to_google_spreadsheet


def capture_lead(lead: LeadRequestSchema) -> bool:
    capture_lead_to_google_spreadsheet(
        LEADS_GOOGLE_SPREADSHEET_ID,
        [lead.name, lead.address, lead.phone]
    )
    return True
