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

google_spreadsheet_file_id = "15mpbPy9UQvnVZkWgXgSBYipHhgUC4uS7kMxZawqNvW8"


def capture_lead(lead: LeadRequestSchema):
    gc = gspread.service_account_from_dict(credentials, scopes)

    sheet = gc.open_by_key(google_spreadsheet_file_id)
    sheet.values_append("A1", {"valueInputOption": "RAW"}, {
        # Array of arrays. Outer array: rows. Innter array: columns.
        "values": [[lead.name, lead.address, lead.phone]]
    })

    return True
