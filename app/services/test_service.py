import uuid
from typing import Annotated

from fastapi import Depends

from app.backend.db.dependencies import get_repository
from app.backend.db.models.customer import Customer
from app.backend.db.repository import DatabaseRepository
from app.repositories.customer_repository import CustomerRepository


class TestService:
    def __init__(
        self,
        customer_repository: Annotated[CustomerRepository, Depends(CustomerRepository)],
    ):
        self.customer_repository = customer_repository

    async def get_customer(self, id: uuid.UUID):
        return await self.customer_repository.get(id)
