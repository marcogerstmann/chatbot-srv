from typing import Final

# Open API
OPEN_API_TITLE: Final = "Solar Chatbot Service"
OPEN_API_DESCRIPTION: Final = "API and backend for the solar industry chatbot."

# Google Solar API
MIN_SOLAR_API_IMAGE_QUALITY: Final = "MEDIUM"  # "LOW" | "MEDIUM" | "HIGH"

# Solar potential calculations
DC_TO_AC_RATE = 0.85
AVG_COST_PER_KWH = 0.26  # TODO: Move to DB or external api, because it changes more frequently

# Google Drive Resources
VECTOR_SOURCES_BASE_FOLDER_ID = "1Z7WKT8-iiOpuAibGjlFpz-fSnodYa1Sh"
LEADS_GOOGLE_SPREADSHEET_ID = "15mpbPy9UQvnVZkWgXgSBYipHhgUC4uS7kMxZawqNvW8"  # TODO: Move to DB (customer specific)
