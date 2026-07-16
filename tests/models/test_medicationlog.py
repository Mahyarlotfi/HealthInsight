"""Tests for the SQLAlchemy MedicationLog model."""

# pylint: disable=missing-function-docstring

import pytest
from sqlalchemy.exc import IntegrityError

from healthinsight.models.medication_log import MedicationLog
from tests.builders import make_medication, make_medication_log
from tests.helper import column_exists


def test_create_medication_log(session):
    """A MedicationLog can be persisted."""
    medication_log = make_medication_log()

    session.add(medication_log)
    session.commit()

    assert medication_log.id is not None


def test_table_name():
    """Verify table name."""
    assert MedicationLog.__tablename__ == "medication_logs"


def test_columns(engine):
    """Verify expected columns exist."""
    expected = (
        "id",
        "medication_id",
        "date",
        "taken",
        "notes",
        "created_at",
        "updated_at",
    )

    for column in expected:
        assert column_exists(engine, "medication_logs", column)


def test_repr():
    """Verify __repr__."""
    medication_log = make_medication_log()

    assert (
        repr(medication_log) == "MedicationLog(id=None, date=datetime.date(2024, 1, 1))"
    )


def test_notes_is_optional(session):
    """notes should be optional."""
    medication_log = make_medication_log(notes=None)

    session.add(medication_log)
    session.commit()

    assert medication_log.notes is None


@pytest.mark.parametrize(
    "field",
    (
        "medication_id",
        "date",
        "taken",
    ),
)
def test_required_fields(session, field):
    """Required fields reject None."""
    medication_log = make_medication_log(**{field: None})

    session.add(medication_log)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_medication_relationship(session):
    medication = make_medication()

    session.add(medication)
    session.commit()

    medication_log = make_medication_log(medication=medication)

    session.add(medication_log)
    session.commit()

    assert medication_log.medication == medication


def test_empty_notes_not_allowed(session):
    medication_log = make_medication_log(notes="   ")

    session.add(medication_log)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_duplicate_medication_date_not_allowed(session):
    medication = make_medication()

    session.add(medication)
    session.commit()

    first = make_medication_log(medication_id=medication.id)
    second = make_medication_log(medication_id=medication.id)

    session.add(first)
    session.commit()

    session.add(second)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()
