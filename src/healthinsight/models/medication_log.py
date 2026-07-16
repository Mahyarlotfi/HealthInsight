"""SQLAlchemy MedicationLog model."""

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from healthinsight.database.base import BaseModel

if TYPE_CHECKING:
    from .medication import Medication


# pylint: disable=too-few-public-methods
class MedicationLog(BaseModel):
    """Represents a medication intake record."""

    __tablename__ = "medication_logs"

    __table_args__ = (
        CheckConstraint(
            "trim(notes) <> '' OR notes IS NULL",
            name="ck_medication_logs_notes_not_empty",
        ),
        UniqueConstraint(
            "medication_id",
            "date",
            name="uq_medication_logs_medication_date",
        ),
        Index(
            "ix_medication_logs_medication_id",
            "medication_id",
        ),
        Index(
            "ix_medication_logs_date",
            "date",
        ),
    )

    medication_id: Mapped[int] = mapped_column(
        ForeignKey("medications.id"),
        nullable=False,
    )

    date: Mapped[datetime.date] = mapped_column(nullable=False)
    taken: Mapped[bool] = mapped_column(nullable=False)
    notes: Mapped[str | None] = mapped_column()

    medication: Mapped["Medication"] = relationship(
        back_populates="medication_logs",
    )

    def __repr__(self):
        return f"MedicationLog(id={self.id}, date={self.date!r})"
