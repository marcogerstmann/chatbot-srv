from fastapi import APIRouter

router = APIRouter(prefix="/info")


@router.get("")
def get_info():
    """Get info"""

    return "Application is up and running!"
