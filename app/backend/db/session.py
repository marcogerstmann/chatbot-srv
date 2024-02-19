from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.backend.settings import get_settings

engine = create_engine(get_settings().postgres_connection_string, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
