from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.db.models.customer import Customer
from app.backend.db.session import get_db_session

router = APIRouter(prefix="/info")


@router.get("")
def get_info():
    """Get info"""

    return "Application is up and running!"


# TODO: Delete. Just an example for fetching from DB
@router.get("/test")
async def test(db_session: AsyncSession = Depends(get_db_session)):
    customer = await db_session.get(Customer, "ddbf04e4-4211-43f8-976a-94cd90c40a0a")
    print(customer.name)
    pass
