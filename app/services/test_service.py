import uuid
from typing import Annotated

from fastapi import Depends

from app.repositories.customer_repository import CustomerRepository


class TestService:
    def __init__(
        self,
        customer_repository: Annotated[CustomerRepository, Depends(CustomerRepository)],
    ):
        self.customer_repository = customer_repository

    def get_customer(self, id: uuid.UUID):
        return self.customer_repository.get(id)
