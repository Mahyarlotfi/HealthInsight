"""Base repository implementation."""

from typing import Generic, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from healthinsight.database.base import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)


class BaseRepository(Generic[ModelType]):
    """Base repository with shared database operations."""

    def __init__(
        self,
        session: Session,
        model: type[ModelType],
    ) -> None:
        """Initialize the repository."""
        self._session = session
        self._model = model

    def get_by_id(self, model_id: int) -> ModelType | None:
        """Return a model by its ID."""
        return self._session.get(self._model, model_id)

    def get_all(self) -> list[ModelType]:
        """Return all models."""
        statement = select(self._model)
        return list(self._session.scalars(statement))

    def add(self, instance: ModelType) -> ModelType:
        """Add a model."""
        try:
            self._session.add(instance)
            self._session.commit()
            self._session.refresh(instance)
            return instance
        except Exception:
            self._session.rollback()
            raise

    def update(self, instance: ModelType) -> ModelType:
        """Update a model."""
        try:
            merged = self._session.merge(instance)
            self._session.commit()
            self._session.refresh(merged)
            return merged
        except Exception:
            self._session.rollback()
            raise

    def delete(self, model_id: int) -> None:
        """Delete a model by its ID."""
        instance = self.get_by_id(model_id)
        if instance is None:
            raise LookupError(f"{self._model.__name__} with id={model_id} not found.")

        try:
            self._session.delete(instance)
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise
