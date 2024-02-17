from sqlalchemy import create_engine

from app.backend.config import config
from app.backend.db.models.base import Base


def migrate_tables() -> bool:
    engine = create_engine(config.postgres_connection_string)
    Base.metadata.create_all(engine)
    return True
