from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse

from app.backend.util.logging import logger
from app.constants import HTTP_HEADER_CHATBOT_ID, HTTP_HEADER_SESSION_ID


async def check_request_headers(request: Request, call_next):
    try:
        if request.url.path.startswith("/admin"):
            # TODO: Protect admin endpoints
            logger.info("Admin endpoint called")

        if request.url.path.startswith("/public"):
            await ensure_request_header(request, HTTP_HEADER_CHATBOT_ID)
            await ensure_request_header(request, HTTP_HEADER_SESSION_ID)

        return await call_next(request)
    except HTTPException as ex:
        return JSONResponse(
            content={"detail": str(ex.detail)}, status_code=ex.status_code
        )


async def ensure_request_header(request: Request, header: str):
    customer_id = request.headers.get(header)
    if customer_id is None or not customer_id.strip():
        raise HTTPException(
            detail=f"Invalid or missing header {header}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
