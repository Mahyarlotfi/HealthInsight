"""Tests for the SQLAlchemy user model."""

from datetime import date

import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from healthinsight.database.base import BaseModel
from healthinsight.models.user import User


def column_exists(engine, table, column):
    """Return True if a column exists in a table."""
    inspector = inspect(engine)

    if table not in inspector.get_table_names():
        return False

    columns = [col["name"] for col in inspector.get_columns(table)]
    return column in columns


def test_create_user():
    """Create and persist a user."""
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    with Session(engine) as session:
        user = User(
            full_name="John Doe",
            date_of_birth=date(1990, 1, 1),
            gender="male",
            height=180,
            initial_weight=75.0,
            target_weight=70.0,
        )
        session.add(user)
        session.commit()
        session.refresh(user)

        assert user.id is not None


def test_user_table_name():
    """Verify the user table name."""
    assert User.__tablename__ == "users"


def test_user_columns():
    """Verify the user table contains all expected columns."""
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    inspector = inspect(engine)

    assert "users" in inspector.get_table_names()
    assert column_exists(engine, "users", "id")
    assert column_exists(engine, "users", "full_name")
    assert column_exists(engine, "users", "date_of_birth")
    assert column_exists(engine, "users", "gender")
    assert column_exists(engine, "users", "height")
    assert column_exists(engine, "users", "initial_weight")
    assert column_exists(engine, "users", "target_weight")
    assert column_exists(engine, "users", "created_at")
    assert column_exists(engine, "users", "updated_at")


def test_user_repr():
    """Verify the string representation of a user."""
    user = User(
        full_name="John Doe",
        date_of_birth=date(1990, 1, 1),
        gender="male",
        height=180,
        initial_weight=75.0,
        target_weight=70.0,
    )

    assert repr(user) == "User(id=None, full_name='John Doe')"


def test_optional_target_weight():
    """Verify target_weight is optional."""
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    with Session(engine) as session:
        user = User(
            full_name="John Doe",
            date_of_birth=date(1990, 1, 1),
            gender="male",
            height=180,
            initial_weight=75.0,
            target_weight=None,
        )
        session.add(user)
        session.commit()
        session.refresh(user)

        assert user.id is not None
        assert user.target_weight is None


def test_required_full_name():
    """Verify full_name is required."""
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            full_name=None,
            date_of_birth=date(1990, 1, 1),
            gender="male",
            height=180,
            initial_weight=75.0,
        )

        session.add(user)

        with pytest.raises(IntegrityError):
            session.commit()


def test_required_date_of_birth():
    """Verify date_of_birth is required."""
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            full_name="John Doe",
            date_of_birth=None,
            gender="male",
            height=180,
            initial_weight=75.0,
        )

        session.add(user)

        with pytest.raises(IntegrityError):
            session.commit()


def test_required_gender():
    """Verify gender is required."""
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            full_name="John Doe",
            date_of_birth=date(1990, 1, 1),
            gender=None,
            height=180,
            initial_weight=75.0,
        )

        session.add(user)

        with pytest.raises(IntegrityError):
            session.commit()


def test_required_height():
    """Verify height is required."""
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            full_name="John Doe",
            date_of_birth=date(1990, 1, 1),
            gender="male",
            height=None,
            initial_weight=75.0,
        )

        session.add(user)

        with pytest.raises(IntegrityError):
            session.commit()


def test_required_initial_weight():
    """Verify initial_weight is required."""
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            full_name="John Doe",
            date_of_birth=date(1990, 1, 1),
            gender="male",
            height=180,
            initial_weight=None,
        )

        session.add(user)

        with pytest.raises(IntegrityError):
            session.commit()
