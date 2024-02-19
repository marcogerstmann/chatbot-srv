from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse

from app.constants import HTTP_HEADER_CHATBOT_ID, HTTP_HEADER_SESSION_ID


async def check_request_headers(request: Request, call_next):
    try:
        if request.url.path.startswith("/admin"):
            # TODO: Protect admin endpoints
            print("Admin endpoint called")

        if request.url.path.startswith("/public"):
            await verify_session_id(request)
            await verify_chatbot_id(request)

        return await call_next(request)
    except HTTPException as ex:
        return JSONResponse(
            content={"detail": str(ex.detail)}, status_code=ex.status_code
        )


async def verify_session_id(request: Request):
    session_id = request.headers.get(HTTP_HEADER_SESSION_ID)
    if session_id is None or not session_id.strip():
        raise HTTPException(
            detail=f"Invalid or missing header {HTTP_HEADER_SESSION_ID}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )


async def verify_chatbot_id(request: Request):
    customer_id = request.headers.get(HTTP_HEADER_CHATBOT_ID)
    # TODO: Also check if customer exists in database
    if customer_id is None or not customer_id.strip():
        raise HTTPException(
            detail=f"Invalid or missing header {HTTP_HEADER_CHATBOT_ID}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
