import uuid

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, server_default=func.gen_random_uuid()
    )


class Customer(Base):
    __tablename__ = "customer"

    number: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    chatbots: Mapped[list["Chatbot"]] = relationship(back_populates="customer")


class Chatbot(Base):
    __tablename__ = "chatbot"

    name: Mapped[str] = mapped_column(nullable=True)
    customer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("customer.id"))
    customer: Mapped["Customer"] = relationship(back_populates="chatbots")
    system_prompt: Mapped[str] = mapped_column(nullable=True)
    vector_scrape_urls: Mapped[list["ChatbotVectorScrapeUrl"]] = relationship(
        back_populates="chatbot"
    )
    vector_chunk_size: Mapped[int] = mapped_column(nullable=True)
    vector_chunk_overlap: Mapped[int] = mapped_column(nullable=True)
    vector_separators: Mapped[str] = mapped_column(nullable=True)
    vector_product_description_html_class: Mapped[str] = mapped_column(nullable=True)


class ChatbotVectorScrapeUrl(Base):
    __tablename__ = "chatbot_vector_scrape_url"

    chatbot_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("chatbot.id"))
    chatbot: Mapped["Chatbot"] = relationship()
    url: Mapped[str] = mapped_column(nullable=False, unique=True)
