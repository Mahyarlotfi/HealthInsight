"""Tests for the SQLAlchemy ProgressPhoto model."""

# pylint: disable=missing-function-docstring

import pytest
from sqlalchemy.exc import IntegrityError

from healthinsight.models.progress_photo import ProgressPhoto
from tests.helper import column_exists
from tests.builders import make_user, make_progress_photo


def test_create_photo(session):
    """A ProgressPhoto can be persisted."""
    photo = make_progress_photo()

    session.add(photo)
    session.commit()

    assert photo.id is not None


def test_table_name():
    """Verify table name."""
    assert ProgressPhoto.__tablename__ == "progress_photos"


def test_columns(engine):
    """Verify expected columns exist."""
    expected = (
        "id",
        "user_id",
        "date",
        "file_path",
        "notes",
        "created_at",
        "updated_at",
    )

    for column in expected:
        assert column_exists(engine, "progress_photos", column)


def test_repr():
    """Verify __repr__."""
    photo = make_progress_photo()

    assert repr(photo) == "ProgressPhoto(id=None, date=datetime.date(2024, 1, 1))"


def test_notes_is_optional(session):
    """notes should be optional."""
    photo = make_progress_photo(notes=None)

    session.add(photo)
    session.commit()

    assert photo.notes is None


@pytest.mark.parametrize(
    "field",
    (
        "user_id",
        "date",
        "file_path",
    ),
)
def test_required_fields(session, field):
    """Required fields reject None."""
    photo = make_progress_photo(**{field: None})

    session.add(photo)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_progress_photo_user_relationship(session):
    user = make_user()
    session.add(user)
    session.commit()

    photo = make_progress_photo(user=user)

    session.add(photo)
    session.commit()

    assert photo.user == user


def test_delete_user_deletes_progress_photos(session):
    user = make_user()
    session.add(user)
    session.commit()

    photo = make_progress_photo(user=user)

    session.add(photo)
    session.commit()

    photo_id = photo.id

    session.delete(user)
    session.commit()

    assert session.get(ProgressPhoto, photo_id) is None


def test_empty_file_path_not_allowed(session):
    photo = make_progress_photo(file_path="   ")

    session.add(photo)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()


def test_unique_user_file_path(session):
    first = make_progress_photo()
    second = make_progress_photo()

    session.add(first)
    session.commit()

    session.add(second)

    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()
