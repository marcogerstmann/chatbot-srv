import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from app.backend.db.dependencies import get_repository
from app.backend.db.models.customer import Customer
from app.backend.db.repository import DatabaseRepository

router = APIRouter(prefix="/test")

# TODO: Delete the test endpoints

CustomerRepository = Annotated[
    DatabaseRepository[Customer],
    Depends(get_repository(Customer)),
]


@router.get("/customers/{id}")
async def test(
    id: uuid.UUID,
    repository: CustomerRepository,  # TODO: Move the dependency injection to service level
):
    customer = await repository.get(id)
    print(customer.name)
    pass
