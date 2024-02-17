from sqlalchemy.orm import Mapped

from app.backend.db.models.base import Base


class Customer(Base):
    __tablename__ = "customer"

    number: Mapped[str]
    name: Mapped[str]
