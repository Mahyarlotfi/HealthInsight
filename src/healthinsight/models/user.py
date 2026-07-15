"""SQLAlchemy User model."""

from datetime import date

from sqlalchemy.orm import Mapped, mapped_column, relationship

from healthinsight.database.base import BaseModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .daily_record import DailyRecord
    from .medication import Medication
    from .activity import Activity
    from .measurement import Measurement
    from .symptom import Symptom
    from .lab_result import LabResult


# pylint: disable=too-few-public-methods
class User(BaseModel):
    """Represents the application user."""

    __tablename__ = "users"
    full_name: Mapped[str] = mapped_column(nullable=False)
    date_of_birth: Mapped[date] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)
    height: Mapped[int] = mapped_column(nullable=False)
    initial_weight: Mapped[float] = mapped_column(nullable=False)
    target_weight: Mapped[float | None] = mapped_column()

    daily_records: Mapped[list["DailyRecord"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    medications: Mapped[list["Medication"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    activities: Mapped[list["Activity"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    measurements: Mapped[list["Measurement"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    symptoms: Mapped[list["Symptom"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    lab_results: Mapped[list["LabResult"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"User(id={self.id}, full_name={self.full_name!r})"
