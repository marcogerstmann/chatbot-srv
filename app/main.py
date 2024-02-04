from fastapi import FastAPI

from app.const import OPEN_API_TITLE, OPEN_API_DESCRIPTION
from app.routers import chat, info

app = FastAPI(
    title=OPEN_API_TITLE,
    description=OPEN_API_DESCRIPTION
)

app.include_router(info.router)
app.include_router(chat.router)
