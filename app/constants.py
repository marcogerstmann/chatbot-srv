from typing import Final

# Open API
OPEN_API_TITLE: Final = "Solar Chatbot Service"
OPEN_API_DESCRIPTION: Final = "API and backend for the solar industry chatbot."

# Google Solar API
MIN_SOLAR_API_IMAGE_QUALITY: Final = "MEDIUM"  # "LOW" | "MEDIUM" | "HIGH"

# Solar potential calculations
DC_TO_AC_RATE: Final = 0.85
AVG_COST_PER_KWH: Final = 0.26  # TODO: Move to DB or external api, because it changes more frequently

# Google Drive Resources
LEADS_GOOGLE_SPREADSHEET_ID: Final = "15mpbPy9UQvnVZkWgXgSBYipHhgUC4uS7kMxZawqNvW8"  # TODO: Move to DB (customer specific)
