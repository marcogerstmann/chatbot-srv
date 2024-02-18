import uuid

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.db import session
from app.backend.db.models.customer import Customer


class CustomerRepository:
    def __init__(self, db: AsyncSession = Depends(session.get_db_session)):
        self.db = db

    async def get(self, id: uuid.UUID):
        return await self.db.get(Customer, id)
