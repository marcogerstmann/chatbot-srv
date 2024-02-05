import gspread

from app.backend.settings import settings
from app.schemas.lead_request_schema import LeadRequestSchema

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = {
    "type": "service_account",
    "private_key": settings.google_service_account_private_key,
    "client_email": settings.google_service_account_email,
    "token_uri": "https://oauth2.googleapis.com/token"
}


def capture_lead(lead: LeadRequestSchema):
    gc = gspread.service_account_from_dict(credentials, scopes)

    # TODO: Capture lead to google sheet
    sh = gc.open("demo-ki-chat-agent-leads")
    print(sh.sheet1.get('A1'))

    return True
