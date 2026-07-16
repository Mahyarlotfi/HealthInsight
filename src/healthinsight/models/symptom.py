"""SQLAlchemy Symptom model."""

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from healthinsight.database.base import BaseModel

if TYPE_CHECKING:
    from .user import User


# pylint: disable=too-few-public-methods
class Symptom(BaseModel):
    """Represents a symptom or side effect reported by the user."""

    __tablename__ = "symptoms"

    __table_args__ = (
        CheckConstraint(
            "severity BETWEEN 1 AND 10",
            name="ck_symptom_severity_range",
        ),
        CheckConstraint(
            "length(trim(name)) > 0",
            name="ck_symptom_name_not_empty",
        ),
        UniqueConstraint(
            "user_id",
            "date",
            "name",
            name="uq_symptom_user_date_name",
        ),
        Index(
            "ix_symptom_user_id",
            "user_id",
        ),
        Index(
            "ix_symptom_user_date",
            "user_id",
            "date",
        ),
        Index(
            "ix_symptom_user_name",
            "user_id",
            "name",
        ),
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )
    date: Mapped[datetime.date] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    severity: Mapped[int] = mapped_column(nullable=False)
    notes: Mapped[str | None] = mapped_column()

    user: Mapped["User"] = relationship(
        back_populates="symptoms",
    )

    def __repr__(self):
        return f"Symptom(id={self.id}, name={self.name!r})"
