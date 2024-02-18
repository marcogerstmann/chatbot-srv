from collections.abc import Callable

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.db import repository, session
from app.backend.db.models.base import Base as BaseModel


def get_repository(
    model: type[BaseModel],
) -> Callable[[AsyncSession], repository.DatabaseRepository]:
    def func(session: AsyncSession = Depends(session.get_db_session)):
        return repository.DatabaseRepository(model, session)

    return func
