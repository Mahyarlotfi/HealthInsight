"""Tests for the SQLAlchemy Medication model."""

# pylint: disable=missing-function-docstring

import pytest
from sqlalchemy.exc import IntegrityError
from datetime import date

from healthinsight.models.medication import Medication
from healthinsight.models.medication_log import MedicationLog
from tests.helper import column_exists
from tests.builders import make_user, make_medication, make_medication_log


def test_create_medication(session):
    medication = make_medication()

    session.add(medication)
    session.commit()

    assert medication.id is not None


def test_table_name():
    assert Medication.__tablename__ == "medications"


def test_columns(engine):
    expected_columns = (
        "id",
        "user_id",
        "name",
        "dosage",
        "unit",
        "frequency",
        "start_date",
        "end_date",
        "notes",
        "created_at",
        "updated_at",
    )

    for column in expected_columns:
        assert column_exists(engine, "medications", column)


def test_repr():
    medication = make_medication()

    assert repr(medication) == "Medication(id=None, name='Metformin')"


@pytest.mark.parametrize(
    "field,value",
    (
        ("end_date", None),
        ("notes", None),
    ),
)
def test_optional_fields(session, field, value):
    medication = make_medication(**{field: value})

    session.add(medication)
    session.commit()

    assert getattr(medication, field) is value


@pytest.mark.parametrize(
    "field",
    (
        "user_id",
        "name",
        "dosage",
        "unit",
        "frequency",
        "start_date",
    ),
)
def test_required_fields(session, field):
    medication = make_medication(**{field: None})

    session.add(medication)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_medication_user_relationship(session):
    """Medication is linked to its user."""
    user = make_user()

    session.add(user)
    session.commit()

    medication = make_medication(user=user)

    session.add(medication)
    session.commit()

    assert medication.user == user


def test_negative_dosage_not_allowed(session):
    """Dosage must be positive."""
    medication = make_medication(dosage=-100)

    session.add(medication)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_end_date_before_start_date_not_allowed(session):
    """End date cannot be before start date."""
    medication = make_medication(
        start_date=date(2024, 12, 31),
        end_date=date(2024, 1, 1),
    )

    session.add(medication)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_duplicate_medication_not_allowed(session):
    """Same medication cannot be duplicated for a user."""
    medication1 = make_medication()
    medication2 = make_medication()

    session.add(medication1)
    session.commit()

    session.add(medication2)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_medication_logs_relationship(session):
    medication = make_medication()

    session.add(medication)
    session.commit()

    medication_log = make_medication_log(medication=medication)

    session.add(medication_log)
    session.commit()

    assert medication_log in medication.medication_logs


def test_delete_medication_deletes_logs(session):
    medication = make_medication()

    session.add(medication)
    session.commit()

    medication_log = make_medication_log(medication=medication)

    session.add(medication_log)
    session.commit()

    session.delete(medication)
    session.commit()

    assert session.get(MedicationLog, medication_log.id) is None
