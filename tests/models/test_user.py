"""Tests for the SQLAlchemy User model."""

# pylint: disable=missing-function-docstring

import pytest
from sqlalchemy.exc import IntegrityError

from healthinsight.models.user import User
from healthinsight.models.daily_record import DailyRecord
from tests.helper import column_exists
from tests.builders import make_user, make_daily_record, make_medication


def test_create_user(session):
    user = make_user()

    session.add(user)
    session.commit()

    assert user.id is not None


def test_table_name():
    assert User.__tablename__ == "users"


def test_columns(engine):
    expected_columns = (
        "id",
        "full_name",
        "date_of_birth",
        "gender",
        "height",
        "initial_weight",
        "target_weight",
        "created_at",
        "updated_at",
    )

    for column in expected_columns:
        assert column_exists(engine, "users", column)


def test_repr():
    user = make_user()

    assert repr(user) == "User(id=None, full_name='John Doe')"


def test_target_weight_is_optional(session):
    user = make_user(target_weight=None)

    session.add(user)
    session.commit()

    assert user.target_weight is None


@pytest.mark.parametrize(
    "field",
    (
        "full_name",
        "date_of_birth",
        "gender",
        "height",
        "initial_weight",
    ),
)
def test_required_fields(session, field):
    kwargs = {field: None}

    session.add(make_user(**kwargs))

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_user_daily_records_relationship(session):
    """User contains its daily records."""
    user = make_user()
    session.add(user)
    session.commit()

    record = make_daily_record(user=user)

    session.add(record)
    session.commit()

    assert record in user.daily_records


def test_delete_user_deletes_daily_records(session):
    user = make_user()
    session.add(user)
    session.commit()

    record = make_daily_record(user=user)

    session.add(record)
    session.commit()

    session.delete(user)
    session.commit()

    assert session.get(DailyRecord, record.id) is None


def test_user_medications_relationship(session):
    """User contains medications."""
    user = make_user()

    session.add(user)
    session.commit()

    medication = make_medication(user=user)

    session.add(medication)
    session.commit()

    assert medication in user.medications
