"""Database session management."""

from sqlalchemy.orm import sessionmaker

from healthinsight.database.engine import engine

SessionLocal = sessionmaker(bind=engine, autoflush=False)


def get_db():
    """Provide a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
