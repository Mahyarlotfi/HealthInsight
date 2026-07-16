"""SQLAlchemy DailyRecord model."""

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from healthinsight.database.base import BaseModel

if TYPE_CHECKING:
    from .user import User


# pylint: disable=too-few-public-methods
class DailyRecord(BaseModel):
    """Represents a daily record for the user."""

    __tablename__ = "daily_records"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "date",
            name="uq_daily_records_user_date",
        ),
        CheckConstraint(
            "weight >= 0",
            name="ck_daily_records_weight_non_negative",
        ),
        CheckConstraint(
            "systolic_bp > 0",
            name="ck_daily_records_systolic_bp_positive",
        ),
        CheckConstraint(
            "diastolic_bp > 0",
            name="ck_daily_records_diastolic_bp_positive",
        ),
        CheckConstraint(
            "heart_rate > 0",
            name="ck_daily_records_heart_rate_positive",
        ),
        CheckConstraint(
            "blood_glucose >= 0",
            name="ck_daily_records_blood_glucose_non_negative",
        ),
        CheckConstraint(
            "water_intake >= 0",
            name="ck_daily_records_water_intake_non_negative",
        ),
        CheckConstraint(
            "sleep_hours >= 0",
            name="ck_daily_records_sleep_hours_non_negative",
        ),
        CheckConstraint(
            "appetite_score BETWEEN 1 AND 5",
            name="ck_daily_records_appetite_score_range",
        ),
        CheckConstraint(
            "energy_score BETWEEN 1 AND 5",
            name="ck_daily_records_energy_score_range",
        ),
        Index(
            "ix_daily_records_user_date",
            "user_id",
            "date",
        ),
    )

    date: Mapped[datetime.date] = mapped_column(nullable=False)
    weight: Mapped[float | None] = mapped_column()
    systolic_bp: Mapped[int | None] = mapped_column()
    diastolic_bp: Mapped[int | None] = mapped_column()
    heart_rate: Mapped[float | None] = mapped_column()
    blood_glucose: Mapped[int | None] = mapped_column()
    water_intake: Mapped[float | None] = mapped_column()
    sleep_hours: Mapped[int | None] = mapped_column()
    sleep_quality: Mapped[str | None] = mapped_column()
    appetite_score: Mapped[int | None] = mapped_column()
    energy_score: Mapped[int | None] = mapped_column()
    notes: Mapped[str | None] = mapped_column()

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )
    user: Mapped["User"] = relationship(
        back_populates="daily_records",
    )

    def __repr__(self):
        return f"DailyRecord(id={self.id}, date={self.date!r})"
