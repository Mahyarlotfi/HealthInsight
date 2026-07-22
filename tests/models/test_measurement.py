"""Tests for the SQLAlchemy Measurement model."""

# pylint: disable=missing-function-docstring

import pytest
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from tests.builders import make_measurement, make_user
from tests.helper import column_exists

from healthinsight.models.measurement import Measurement


def test_create_measurement(session):
    user = make_user()

    session.add(user)
    session.commit()

    measurement = make_measurement(user=user)

    session.add(measurement)
    session.commit()

    assert measurement.id is not None


def test_table_name():
    assert Measurement.__tablename__ == "measurements"


def test_columns(engine):
    expected_columns = (
        "id",
        "user_id",
        "date",
        "waist",
        "hip",
        "whr",
        "created_at",
        "updated_at",
    )

    for column in expected_columns:
        assert column_exists(engine, "measurements", column)


def test_repr():
    measurement = make_measurement()

    assert repr(measurement) == "Measurement(id=None, date=datetime.date(2024, 1, 1))"


@pytest.mark.parametrize(
    "field",
    (
        "user_id",
        "date",
        "waist",
        "hip",
        "whr",
    ),
)
def test_required_fields(session, field):
    measurement = make_measurement(**{field: None})

    session.add(measurement)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_measurement_user_relationship(session):
    """Measurement is linked to its user."""
    user = make_user()

    session.add(user)
    session.commit()

    measurement = make_measurement(user=user)

    session.add(measurement)
    session.commit()

    assert measurement.user == user


def test_unique_user_date_measurement(session):
    measurement1 = make_measurement()
    measurement2 = make_measurement()

    session.add_all([measurement1, measurement2])

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_waist_must_be_positive(session):
    measurement = make_measurement(waist=0)

    session.add(measurement)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_hip_must_be_positive(session):
    measurement = make_measurement(hip=-1)

    session.add(measurement)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_whr_must_be_positive(session):
    measurement = make_measurement(whr=0)

    session.add(measurement)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_whr_invalid_large_value(session):
    measurement = make_measurement(whr=10)

    session.add(measurement)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_indexes(engine):
    indexes = inspect(engine).get_indexes("measurements")

    names = {index["name"] for index in indexes}

    assert "ix_measurements_user_date" in names
