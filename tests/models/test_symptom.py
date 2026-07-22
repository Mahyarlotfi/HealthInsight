"""Tests for the SQLAlchemy Symptom model."""

# pylint: disable=missing-function-docstring

import pytest
from sqlalchemy.exc import IntegrityError
from tests.builders import make_symptom, make_user
from tests.helper import column_exists

from healthinsight.models.symptom import Symptom


def test_create_symptom(session):
    """A Symptom can be persisted."""
    symptom = make_symptom()

    session.add(symptom)
    session.commit()

    assert symptom.id is not None


def test_table_name():
    """Verify table name."""
    assert Symptom.__tablename__ == "symptoms"


def test_columns(engine):
    """Verify expected columns exist."""
    expected = (
        "id",
        "user_id",
        "date",
        "name",
        "severity",
        "notes",
        "created_at",
        "updated_at",
    )

    for column in expected:
        assert column_exists(engine, "symptoms", column)


def test_repr():
    """Verify __repr__."""
    symptom = make_symptom()

    assert repr(symptom) == "Symptom(id=None, name='Headache')"


def test_notes_is_optional(session):
    """notes should be optional."""
    symptom = make_symptom(notes=None)

    session.add(symptom)
    session.commit()

    assert symptom.notes is None


@pytest.mark.parametrize(
    "field",
    (
        "user_id",
        "date",
        "name",
        "severity",
    ),
)
def test_required_fields(session, field):
    """Required fields reject None."""
    symptom = make_symptom(**{field: None})

    session.add(symptom)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_symptom_user_relationship(session):
    user = make_user()
    session.add(user)
    session.commit()

    symptom = make_symptom(user=user)

    session.add(symptom)
    session.commit()

    assert symptom.user == user


def test_delete_user_deletes_symptoms(session):
    user = make_user()
    session.add(user)
    session.commit()

    symptom = make_symptom(user=user)

    session.add(symptom)
    session.commit()

    symptom_id = symptom.id

    session.delete(user)
    session.commit()

    assert session.get(Symptom, symptom_id) is None


def test_invalid_severity_low(session):
    symptom = make_symptom(severity=0)

    session.add(symptom)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_invalid_severity_high(session):
    symptom = make_symptom(severity=11)

    session.add(symptom)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_unique_user_date_name(session):
    first = make_symptom()

    second = make_symptom()

    session.add(first)
    session.commit()

    session.add(second)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_empty_name_not_allowed(session):
    symptom = make_symptom(name="   ")

    session.add(symptom)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()
