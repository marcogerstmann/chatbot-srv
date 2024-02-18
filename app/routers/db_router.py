from typing import Annotated

from fastapi import APIRouter, Depends

from app.services.db_service import DbService

router = APIRouter(prefix="/db")


# TODO: Migrations should be performed by alembic
@router.post("/migrate", response_model=bool)
def migrate(db_service: Annotated[DbService, Depends(DbService)]) -> bool:
    """Migrate DB schema"""

    return db_service.migrate_tables()


# TODO: Secure these endpoints or implement another private way to create embeddings
@router.post("/embeddings", response_model=bool)
def post_embeddings(db_service: Annotated[DbService, Depends(DbService)]) -> bool:
    """Create embeddings"""

    return db_service.sync_embeddings()
