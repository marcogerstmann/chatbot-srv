import uuid
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.backend.db.models import Chatbot
from app.backend.db.session import get_db_session


class ChatbotRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.db = db

    def get(self, id: uuid.UUID):
        return self.db.get(Chatbot, id)
