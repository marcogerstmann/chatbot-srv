import uuid
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.backend.db.models import Customer
from app.backend.db.session import get_db_session


class CustomerRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.db = db

    def get(self, id: uuid.UUID):
        return self.db.get(Customer, id)
