"""Unit tests for UserRepository."""

from healthinsight.repositories.user import UserRepository
from tests.builders import make_user


def test_get_by_full_name(session):
    """Return users with the given full name."""
    repository = UserRepository(session)

    repository.add(make_user())
    repository.add(make_user(initial_weight=80.0))
    repository.add(make_user(full_name="Jane Doe"))

    results = repository.get_by_full_name("John Doe")

    assert len(results) == 2
    assert all(user.full_name == "John Doe" for user in results)


def test_get_by_full_name_not_found(session):
    """Return an empty list when no user matches the full name."""
    repository = UserRepository(session)

    repository.add(make_user())

    results = repository.get_by_full_name("Unknown User")

    assert results == []
