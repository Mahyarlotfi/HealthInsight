"""Tests for the SQLAlchemy LabResult model."""

# pylint: disable=missing-function-docstring

import pytest
from sqlalchemy.exc import IntegrityError
from tests.builders import make_lab_result, make_user
from tests.helper import column_exists

from healthinsight.models.lab_result import LabResult


def test_create_lab_result(session):
    """A LabResult can be persisted."""
    lab_result = make_lab_result()

    session.add(lab_result)
    session.commit()

    assert lab_result.id is not None


def test_table_name():
    """Verify table name."""
    assert LabResult.__tablename__ == "lab_results"


def test_columns(engine):
    """Verify expected columns exist."""
    expected = (
        "id",
        "user_id",
        "date",
        "test_name",
        "value",
        "unit",
        "notes",
        "created_at",
        "updated_at",
    )

    for column in expected:
        assert column_exists(engine, "lab_results", column)


def test_repr():
    """Verify __repr__."""
    lab_result = make_lab_result()

    assert repr(lab_result) == "LabResult(id=None, test_name='Fasting Blood Sugar')"


@pytest.mark.parametrize(
    "field",
    (
        "unit",
        "notes",
    ),
)
def test_optional_fields(session, field):
    """Optional fields accept None."""
    lab_result = make_lab_result(**{field: None})

    session.add(lab_result)
    session.commit()

    assert getattr(lab_result, field) is None


@pytest.mark.parametrize(
    "field",
    (
        "user_id",
        "date",
        "test_name",
        "value",
    ),
)
def test_required_fields(session, field):
    """Required fields reject None."""
    lab_result = make_lab_result(**{field: None})

    session.add(lab_result)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_lab_result_user_relationship(session):
    user = make_user()
    session.add(user)
    session.commit()

    lab_result = make_lab_result(user=user)

    session.add(lab_result)
    session.commit()

    assert lab_result.user == user


def test_delete_user_deletes_lab_results(session):
    user = make_user()
    session.add(user)
    session.commit()

    lab_result = make_lab_result(user=user)

    session.add(lab_result)
    session.commit()

    lab_result_id = lab_result.id

    session.delete(user)
    session.commit()

    assert session.get(LabResult, lab_result_id) is None


def test_negative_value_not_allowed(session):
    record = make_lab_result(value=-1)

    session.add(record)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_unique_user_date_test_name(session):
    first = make_lab_result()

    second = make_lab_result()

    session.add(first)
    session.commit()

    session.add(second)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_empty_test_name_not_allowed(session):
    lab_result = make_lab_result(test_name="   ")

    session.add(lab_result)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()
