from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse

from app.backend.settings import get_settings
from app.constants import HTTP_HEADER_CHATBOT_ID, HTTP_HEADER_SESSION_ID


async def check_request_headers(request: Request, call_next):
    try:
        if request.url.path.startswith("/admin"):
            await ensure_admin_auth_header(request)

        if request.url.path.startswith("/public"):
            await ensure_request_header(request, HTTP_HEADER_CHATBOT_ID)
            await ensure_request_header(request, HTTP_HEADER_SESSION_ID)

        return await call_next(request)
    except HTTPException as ex:
        return JSONResponse(
            content={"detail": str(ex.detail)}, status_code=ex.status_code
        )


async def ensure_admin_auth_header(request: Request):
    expected_header = get_settings().admin_api_key
    actual_header = request.headers.get("Authorization")
    if (
        expected_header is None
        or not expected_header.strip()
        or expected_header != actual_header
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


async def ensure_request_header(request: Request, header: str):
    customer_id = request.headers.get(header)
    if customer_id is None or not customer_id.strip():
        raise HTTPException(
            detail=f"Invalid or missing header {header}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
