from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


def add_as_row_to_google_spreadsheet(spreadsheet_id: str, values: list[str]):
    google_service = build(
        "sheets",
        "v4",
        credentials=Credentials.from_service_account_file(
            "google-service-account-key.json",
            scopes=["https://www.googleapis.com/auth/spreadsheets"],
        ),
    )

    (
        google_service.spreadsheets()
        .values()
        .append(
            spreadsheetId=spreadsheet_id,
            range="A1",
            valueInputOption="RAW",
            body={
                # Array of arrays. Outer array: rows. Innter array: columns.
                "values": [values]
            },
        )
        .execute()
    )
