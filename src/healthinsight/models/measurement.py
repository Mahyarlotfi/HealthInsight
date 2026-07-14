"""SQLAlchemy Measurement model."""

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
class Measurement(BaseModel):
    """Represents a measurement taken by the user."""

    __tablename__ = "measurements"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "date",
            name="uq_measurements_user_date",
        ),
        CheckConstraint(
            "waist > 0",
            name="ck_measurements_waist_positive",
        ),
        CheckConstraint(
            "hip > 0",
            name="ck_measurements_hip_positive",
        ),
        CheckConstraint(
            "whr > 0 AND whr < 3",
            name="ck_measurements_whr_valid",
        ),
        Index(
            "ix_measurements_user_date",
            "user_id",
            "date",
        ),
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    date: Mapped[datetime.date] = mapped_column(nullable=False)
    waist: Mapped[float] = mapped_column(nullable=False)
    hip: Mapped[float] = mapped_column(nullable=False)
    whr: Mapped[float] = mapped_column(nullable=False)

    user: Mapped["User"] = relationship(
        back_populates="measurements",
    )

    def __repr__(self):
        return f"Measurement(id={self.id}, date={self.date!r})"
