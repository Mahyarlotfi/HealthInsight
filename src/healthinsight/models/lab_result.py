"""SQLAlchemy LabResult model."""

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from healthinsight.database.base import BaseModel

if TYPE_CHECKING:
    from .user import User


# pylint: disable=too-few-public-methods
class LabResult(BaseModel):
    """Represents a lab test result for the user."""

    __tablename__ = "lab_results"

    __table_args__ = (
        CheckConstraint(
            "length(trim(test_name)) > 0",
            name="ck_lab_result_test_name_not_empty",
        ),
        CheckConstraint(
            "value >= 0",
            name="ck_lab_result_value_non_negative",
        ),
        UniqueConstraint(
            "user_id",
            "date",
            "test_name",
            name="uq_lab_result_user_date_test",
        ),
        Index(
            "ix_lab_result_user_id",
            "user_id",
        ),
        Index(
            "ix_lab_result_user_date",
            "user_id",
            "date",
        ),
        Index(
            "ix_lab_result_user_test_name",
            "user_id",
            "test_name",
        ),
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )
    date: Mapped[datetime.date] = mapped_column(nullable=False)
    test_name: Mapped[str] = mapped_column(nullable=False)
    value: Mapped[float] = mapped_column(nullable=False)
    unit: Mapped[str | None] = mapped_column()
    notes: Mapped[str | None] = mapped_column()

    user: Mapped["User"] = relationship(
        back_populates="lab_results",
    )

    def __repr__(self):
        return f"LabResult(id={self.id}, test_name={self.test_name!r})"
