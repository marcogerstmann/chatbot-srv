from fastapi import APIRouter

from app.services.db_service import migrate_tables
from app.services.embeddings_service import sync_embeddings

router = APIRouter(prefix="/db")


# TODO: Migrations should be performed by alembic
@router.post("/migrate", response_model=bool)
def migrate() -> bool:
    """Migrate DB schema"""

    return migrate_tables()


# TODO: Secure these endpoints or implement another private way to create embeddings
@router.post("/embeddings", response_model=bool)
def post_embeddings() -> bool:
    """Create embeddings"""

    return sync_embeddings()
