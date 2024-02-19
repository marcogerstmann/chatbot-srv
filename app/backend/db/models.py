import uuid

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, server_default=func.gen_random_uuid()
    )


class Customer(Base):
    __tablename__ = "customer"

    number: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    chatbots: Mapped[list["Chatbot"]] = relationship(back_populates="customer")


class Chatbot(Base):
    __tablename__ = "chatbot"

    name: Mapped[str] = mapped_column(nullable=True)
    customer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("customer.id"))
    customer: Mapped["Customer"] = relationship(back_populates="chatbots")
