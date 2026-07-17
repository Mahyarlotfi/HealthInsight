"""Unit tests for the BaseRepository class."""

import pytest
from sqlalchemy.orm import Mapped, mapped_column

from healthinsight.database.base import BaseModel
from healthinsight.repositories.base import BaseRepository


# pylint: disable=too-few-public-methods
class RepositoryTestModel(BaseModel):
    """Model used for testing."""

    __tablename__ = "repository_test_models"

    name: Mapped[str] = mapped_column()


def test_get_by_id(session):
    """Return a model by its ID."""
    repository = BaseRepository(session, RepositoryTestModel)

    instance = RepositoryTestModel(name="John Doe")

    result = repository.add(instance)

    get_result = repository.get_by_id(result.id)

    assert get_result is not None
    assert get_result.id == result.id
    assert get_result.name == "John Doe"


def test_get_all(session):
    """Return all models."""
    repository = BaseRepository(session, RepositoryTestModel)

    repository.add(RepositoryTestModel(name="John Doe"))
    repository.add(RepositoryTestModel(name="Jane Doe"))

    results = repository.get_all()

    assert len(results) == 2
    assert results[0].name == "John Doe"
    assert results[1].name == "Jane Doe"


def test_add(session):
    """Add a model to the database."""
    repository = BaseRepository(session, RepositoryTestModel)

    instance = RepositoryTestModel(name="John Doe")

    result = repository.add(instance)

    assert result.id is not None
    assert result.name == "John Doe"

    saved = session.get(RepositoryTestModel, result.id)

    assert saved is not None
    assert saved.name == "John Doe"


def test_update(session):
    """Update an existing model."""
    repository = BaseRepository(session, RepositoryTestModel)

    instance = RepositoryTestModel(name="John Doe")

    result = repository.add(instance)

    assert result.id is not None
    assert result.name == "John Doe"

    result.name = "Petrov"

    update_result = repository.update(result)

    assert update_result.name == "Petrov"

    saved = session.get(RepositoryTestModel, result.id)

    assert saved is not None
    assert saved.name == "Petrov"


def test_delete(session):
    """Delete a model by its ID."""
    repository = BaseRepository(session, RepositoryTestModel)

    instance = RepositoryTestModel(name="John Doe")

    result = repository.add(instance)

    assert repository.get_by_id(result.id) is not None

    repository.delete(result.id)

    assert repository.get_by_id(result.id) is None


def test_delete_not_found(session):
    """Raise LookupError when deleting a non-existent model."""
    repository = BaseRepository(session, RepositoryTestModel)

    with pytest.raises(LookupError):
        repository.delete(999)
