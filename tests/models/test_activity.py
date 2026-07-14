"""Tests for the SQLAlchemy Activity model."""

# pylint: disable=missing-function-docstring

import pytest
from sqlalchemy.exc import IntegrityError

from healthinsight.models.activity import Activity
from tests.helper import column_exists
from tests.builders import make_user, make_activity


def test_create_activity(session):
    activity = make_activity()

    session.add(activity)
    session.commit()

    assert activity.id is not None


def test_table_name():
    assert Activity.__tablename__ == "activities"


def test_columns(engine):
    expected_columns = (
        "id",
        "user_id",
        "date",
        "activity_type",
        "duration",
        "intensity",
        "distance",
        "calories",
        "notes",
        "created_at",
        "updated_at",
    )

    for column in expected_columns:
        assert column_exists(engine, "activities", column)


def test_repr():
    activity = make_activity()

    assert repr(activity) == "Activity(id=None, activity_type='Walking')"


@pytest.mark.parametrize(
    "field,value",
    (
        ("intensity", None),
        ("distance", None),
        ("calories", None),
        ("notes", None),
    ),
)
def test_optional_fields(session, field, value):
    activity = make_activity(**{field: value})

    session.add(activity)
    session.commit()

    assert getattr(activity, field) is value


@pytest.mark.parametrize(
    "field",
    (
        "user_id",
        "date",
        "activity_type",
        "duration",
    ),
)
def test_required_fields(session, field):
    activity = make_activity(**{field: None})

    session.add(activity)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_activity_user_relationship(session):
    """Activity is linked to its user."""
    user = make_user()

    session.add(user)
    session.commit()

    activity = make_activity(user=user)

    session.add(activity)
    session.commit()

    assert activity.user == user


def test_unique_user_date_activity(session):
    activity1 = make_activity()

    activity2 = make_activity()

    session.add_all([activity1, activity2])

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_duration_must_be_positive(session):
    activity = make_activity(duration=0)

    session.add(activity)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_distance_cannot_be_negative(session):
    activity = make_activity(distance=-1)

    session.add(activity)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_calories_cannot_be_negative(session):
    activity = make_activity(calories=-10)

    session.add(activity)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_invalid_intensity_not_allowed(session):
    activity = make_activity(intensity="Very High")

    session.add(activity)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()
