# pylint: disable=too-few-public-methods
"""Shared SQLAlchemy base classes."""

from datetime import datetime, timezone

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


def utcnow():
    """Return the current UTC time as a timezone-aware datetime."""
    return datetime.now(timezone.utc)


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""


class TimestampMixin:
    """Mixin that provides timestamp fields."""

    __abstract__ = True
    created_at: Mapped[datetime] = mapped_column(default=utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=utcnow, onupdate=utcnow)


class BaseModel(TimestampMixin, Base):
    """Abstract base model with shared fields."""

    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
