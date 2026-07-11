"""Tests for the shared SQLAlchemy base model."""

import time

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Mapped, Session, mapped_column

from healthinsight.database.base import BaseModel


# pylint: disable=too-few-public-methods
class SampleModel(BaseModel):
    """Model used for testing."""

    __tablename__ = "test_models"

    name: Mapped[str] = mapped_column()


def column_exists(engine, table, column):
    """Return True if a column exists in a table."""
    inspector = inspect(engine)

    if table not in inspector.get_table_names():
        return False

    columns = [col["name"] for col in inspector.get_columns(table)]
    return column in columns


def test_create_table():
    """Create the test table."""
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)

    inspector = inspect(engine)

    assert "test_models" in inspector.get_table_names()


def test_column_exists():
    """Return True for an existing column."""
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)

    assert column_exists(engine, "test_models", "id")
    assert column_exists(engine, "test_models", "name")
    assert column_exists(engine, "test_models", "created_at")
    assert column_exists(engine, "test_models", "updated_at")


def test_missing_column():
    """Return False for a missing column."""
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)

    assert not column_exists(engine, "test_models", "missing")


def test_missing_table():
    """Return False for a missing table."""
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)

    assert not column_exists(engine, "missing_table", "name")


def test_timestamp_update():
    """Update only updated_at after modifying a record."""
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)

    with Session(engine) as session:
        record = SampleModel(name="original")
        session.add(record)
        session.commit()
        session.refresh(record)

        assert record.created_at is not None
        assert record.updated_at is not None

        created_at = record.created_at
        updated_at = record.updated_at

        time.sleep(0.01)

        record.name = "changed"
        session.commit()
        session.refresh(record)

        assert record.created_at == created_at
        assert record.updated_at > updated_at
