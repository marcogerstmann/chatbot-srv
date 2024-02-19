import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from app.services.test_service import TestService

router = APIRouter(prefix="/test")

# TODO: Delete the test endpoints


@router.get("/customers/{id}")
def test(id: uuid.UUID, test_service: Annotated[TestService, Depends(TestService)]):
    customer = test_service.get_customer(id)
    print(customer.name)
    print(customer.chatbots[0].name)
    pass
