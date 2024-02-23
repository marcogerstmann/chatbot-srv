import uuid
from typing import Final

# Custom http headers
HTTP_HEADER_CHATBOT_ID: Final = "x-chatbot-id"
HTTP_HEADER_SESSION_ID: Final = "x-session-id"

# Open API
OPEN_API_TITLE: Final = '"hi ai" Chatbot Service'
OPEN_API_DESCRIPTION: Final = 'API and backend for "hi ai" chatbots.'

# Internal or special chatbots
CHATBOT_AVA_ID: Final = uuid.UUID("35bdc802-495e-4fc6-8ca6-fb176c08a777")
