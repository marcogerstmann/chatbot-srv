from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from app.backend.middleware.check_request_headers import check_request_headers
from app.constants import OPEN_API_DESCRIPTION, OPEN_API_TITLE
from app.routers import (
    chat_router,
    embeddings_router,
    info_router,
    leads_router,
    solar_router,
)

app = FastAPI(title=OPEN_API_TITLE, description=OPEN_API_DESCRIPTION)

app.add_middleware(BaseHTTPMiddleware, dispatch=check_request_headers)

app.include_router(info_router.router)
app.include_router(embeddings_router.router, prefix="/admin")
app.include_router(chat_router.router, prefix="/public")
app.include_router(solar_router.router, prefix="/public")
app.include_router(leads_router.router, prefix="/public")
