from app.schemas.lead_request_schema import LeadRequestSchema
from app.services.google_api_service import capture_lead_to_google_spreadsheet

leads_google_spreadsheet_id = "15mpbPy9UQvnVZkWgXgSBYipHhgUC4uS7kMxZawqNvW8"


def capture_lead(lead: LeadRequestSchema) -> bool:
    capture_lead_to_google_spreadsheet(
        leads_google_spreadsheet_id,
        [lead.name, lead.address, lead.phone]
    )
    return True
