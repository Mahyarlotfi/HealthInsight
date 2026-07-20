"""Tests for DailyRecordRepository."""

from datetime import date

from healthinsight.repositories.daily_record import (
    DailyRecordRepository,
)
from tests.builders import make_daily_record, make_user


def test_get_by_user(session):
    """Return all records for the given user."""
    repository = DailyRecordRepository(session)

    user1 = make_user()
    user2 = make_user(full_name="Jane Doe")

    session.add_all([user1, user2])
    session.flush()

    repository.add(
        make_daily_record(
            user_id=user1.id,
            date=date(2025, 1, 1),
        )
    )
    repository.add(
        make_daily_record(
            user_id=user1.id,
            date=date(2025, 1, 2),
        )
    )
    repository.add(
        make_daily_record(
            user_id=user2.id,
            date=date(2025, 1, 3),
        )
    )

    results = repository.get_by_user(user1.id)

    assert len(results) == 2
    assert all(record.user_id == user1.id for record in results)


def test_get_by_user_not_found(session):
    """Return an empty list when the user has no records."""
    repository = DailyRecordRepository(session)

    results = repository.get_by_user(999)

    assert results == []


def test_get_by_date(session):
    """Return all records for the given date."""
    repository = DailyRecordRepository(session)

    user1 = make_user()
    user2 = make_user(full_name="Jane Doe")

    session.add_all([user1, user2])
    session.flush()

    repository.add(
        make_daily_record(
            user_id=user1.id,
            date=date(2025, 1, 1),
        )
    )
    repository.add(
        make_daily_record(
            user_id=user2.id,
            date=date(2025, 1, 1),
            weight=80.0,
        )
    )
    repository.add(
        make_daily_record(
            user_id=user1.id,
            date=date(2025, 1, 2),
        )
    )

    results = repository.get_by_date(date(2025, 1, 1))

    assert len(results) == 2
    assert all(record.date == date(2025, 1, 1) for record in results)


def test_get_by_date_not_found(session):
    """Return an empty list when no records exist for the date."""
    repository = DailyRecordRepository(session)

    results = repository.get_by_date(date(2030, 1, 1))

    assert results == []


def test_get_by_date_range(session):
    """Return all records within the given date range."""
    repository = DailyRecordRepository(session)

    user = make_user()

    session.add(user)
    session.flush()

    repository.add(
        make_daily_record(
            user_id=user.id,
            date=date(2025, 1, 1),
        )
    )
    repository.add(
        make_daily_record(
            user_id=user.id,
            date=date(2025, 1, 2),
        )
    )
    repository.add(
        make_daily_record(
            user_id=user.id,
            date=date(2025, 1, 3),
        )
    )

    results = repository.get_by_date_range(
        date(2025, 1, 1),
        date(2025, 1, 2),
    )

    assert len(results) == 2
    assert results[0].date == date(2025, 1, 1)
    assert results[1].date == date(2025, 1, 2)


def test_get_by_date_range_no_results(session):
    """Return an empty list when the date range contains no records."""
    repository = DailyRecordRepository(session)

    results = repository.get_by_date_range(
        date(2030, 1, 1),
        date(2030, 1, 31),
    )

    assert results == []
