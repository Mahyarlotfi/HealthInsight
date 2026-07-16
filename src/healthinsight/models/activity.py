"""SQLAlchemy Activity model."""

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from healthinsight.database.base import BaseModel

if TYPE_CHECKING:
    from .user import User


# pylint: disable=too-few-public-methods
class Activity(BaseModel):
    """Represents a user activity."""

    __tablename__ = "activities"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "date",
            "activity_type",
            "duration",
            name="uq_activities_user_date_type_duration",
        ),
        CheckConstraint(
            "duration > 0",
            name="ck_activities_duration_positive",
        ),
        CheckConstraint(
            "distance IS NULL OR distance >= 0",
            name="ck_activities_distance_non_negative",
        ),
        CheckConstraint(
            "calories IS NULL OR calories >= 0",
            name="ck_activities_calories_non_negative",
        ),
        CheckConstraint(
            "intensity IN ('Low', 'Medium', 'High')",
            name="ck_activities_intensity",
        ),
        Index(
            "ix_activities_user_date",
            "user_id",
            "date",
        ),
        Index(
            "ix_activities_activity_type",
            "activity_type",
        ),
    )

    date: Mapped[datetime.date] = mapped_column(nullable=False)
    activity_type: Mapped[str] = mapped_column(nullable=False)
    duration: Mapped[int] = mapped_column(nullable=False)
    intensity: Mapped[str | None] = mapped_column()
    distance: Mapped[float | None] = mapped_column()
    calories: Mapped[int | None] = mapped_column()
    notes: Mapped[str | None] = mapped_column()

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )
    user: Mapped["User"] = relationship(
        back_populates="activities",
    )

    def __repr__(self):
        return f"Activity(id={self.id}, activity_type={self.activity_type!r})"
