"""for the SQLAlchemy DailyRecord model."""

# pylint: disable=missing-function-docstring

import pytest
from sqlalchemy.exc import IntegrityError

from healthinsight.models.daily_record import DailyRecord
from tests.helper import column_exists
from tests.builders import make_user
from tests.builders import make_daily_record


def test_create_daily_record(session):
    """A DailyRecord can be persisted."""
    record = make_daily_record()

    session.add(record)
    session.commit()

    assert record.id is not None


def test_table_name():
    """Verify table name."""
    assert DailyRecord.__tablename__ == "daily_records"


def test_columns(engine):
    """Verify expected columns exist."""
    expected = (
        "id",
        "user_id",
        "date",
        "weight",
        "systolic_bp",
        "diastolic_bp",
        "heart_rate",
        "blood_glucose",
        "water_intake",
        "sleep_hours",
        "sleep_quality",
        "appetite_score",
        "energy_score",
        "notes",
        "created_at",
        "updated_at",
    )

    for column in expected:
        assert column_exists(engine, "daily_records", column)


def test_repr():
    """Verify __repr__."""
    record = make_daily_record()

    assert repr(record) == "DailyRecord(id=None, date=datetime.date(2024, 1, 1))"


@pytest.mark.parametrize(
    "field",
    (
        "weight",
        "systolic_bp",
        "diastolic_bp",
        "heart_rate",
        "blood_glucose",
        "water_intake",
        "sleep_hours",
        "sleep_quality",
        "appetite_score",
        "energy_score",
        "notes",
    ),
)
def test_optional_fields(session, field):
    """Optional fields accept None."""
    record = make_daily_record(**{field: None})

    session.add(record)
    session.commit()

    assert getattr(record, field) is None


@pytest.mark.parametrize(
    "field",
    (
        "user_id",
        "date",
    ),
)
def test_required_fields(session, field):
    """Required fields reject None."""
    record = make_daily_record(**{field: None})

    session.add(record)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_daily_record_user_relationship(session):
    """DailyRecord is linked to its user."""
    user = make_user()
    session.add(user)
    session.commit()

    record = make_daily_record(user=user)

    session.add(record)
    session.commit()

    assert record.user == user


def test_user_cannot_have_two_daily_records_same_date(session):
    """User cannot have multiple daily records on the same date."""
    user = make_user()

    session.add(user)
    session.commit()

    first_record = make_daily_record(user=user)
    second_record = make_daily_record(user=user)

    session.add_all([first_record, second_record])

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_weight_cannot_be_negative(session):
    """Weight cannot be negative."""
    record = make_daily_record(weight=-1)

    session.add(record)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


@pytest.mark.parametrize("score", [0, 6])
def test_appetite_score_range(session, score):
    """Appetite score must be between 1 and 5."""
    record = make_daily_record(appetite_score=score)

    session.add(record)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


@pytest.mark.parametrize("score", [0, 6])
def test_energy_score_range(session, score):
    """Energy score must be between 1 and 5."""
    record = make_daily_record(energy_score=score)

    session.add(record)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


@pytest.mark.parametrize(
    ("field", "value"),
    (
        ("systolic_bp", 0),
        ("diastolic_bp", 0),
        ("heart_rate", 0),
        ("blood_glucose", -1),
        ("water_intake", -1),
        ("sleep_hours", -1),
    ),
)
def test_health_values_constraints(session, field, value):
    """Health values must be valid."""
    record = make_daily_record(**{field: value})

    session.add(record)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()
