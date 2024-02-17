from collections.abc import AsyncGenerator

from sqlalchemy import exc
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.backend.config import config


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(config.postgres_connection_string_async)
    factory = async_sessionmaker(engine)
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except exc.SQLAlchemyError as error:
            print(f"SQLAlchemy error: {error}")  # TODO: Use logger
            await session.rollback()
            raise
