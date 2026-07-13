# pylint: disable=redefined-outer-name
"""Shared pytest fixtures."""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from healthinsight.database.base import BaseModel


@pytest.fixture(scope="function")
def engine():
    """Create an in-memory SQLite database."""
    engine = create_engine("sqlite:///:memory:")

    BaseModel.metadata.create_all(engine)

    yield engine

    BaseModel.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture(scope="function")
def session(engine):
    """Return a SQLAlchemy session."""
    session_factory = sessionmaker(bind=engine)
    session = session_factory()

    yield session

    session.rollback()
    session.close()
