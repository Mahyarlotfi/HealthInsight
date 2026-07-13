"""SQLAlchemy Medication model."""

from typing import TYPE_CHECKING
import datetime

from sqlalchemy import (
    CheckConstraint,
    ForeignKey,
    Index,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from healthinsight.database.base import BaseModel

if TYPE_CHECKING:
    from .user import User


# pylint: disable=too-few-public-methods
class Medication(BaseModel):
    """Represents a medication taken by the user."""

    __tablename__ = "medications"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "name",
            "start_date",
            name="uq_medications_user_name_start_date",
        ),
        CheckConstraint(
            "dosage > 0",
            name="ck_medications_dosage_positive",
        ),
        CheckConstraint(
            "end_date IS NULL OR end_date >= start_date",
            name="ck_medications_date_range",
        ),
        Index(
            "ix_medications_user_id",
            "user_id",
        ),
        Index(
            "ix_medications_name",
            "name",
        ),
    )

    name: Mapped[str] = mapped_column(nullable=False)
    dosage: Mapped[float] = mapped_column(nullable=False)
    unit: Mapped[str] = mapped_column(nullable=False)
    frequency: Mapped[str] = mapped_column(nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(nullable=False)
    end_date: Mapped[datetime.date | None] = mapped_column()
    notes: Mapped[str | None] = mapped_column()

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )
    user: Mapped["User"] = relationship(
        back_populates="medications",
    )

    def __repr__(self):
        return f"Medication(id={self.id}, name={self.name!r})"
