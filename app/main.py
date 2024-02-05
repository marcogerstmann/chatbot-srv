from fastapi import FastAPI

from app.constants import OPEN_API_TITLE, OPEN_API_DESCRIPTION
from app.routers import chat_router, info_router, embeddings_router, solar_router, leads_router

app = FastAPI(
    title=OPEN_API_TITLE,
    description=OPEN_API_DESCRIPTION
)

app.include_router(info_router.router)
app.include_router(embeddings_router.router)
app.include_router(chat_router.router)
app.include_router(solar_router.router)
app.include_router(leads_router.router)
