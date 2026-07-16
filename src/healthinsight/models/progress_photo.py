"""SQLAlchemy ProgressPhoto model."""

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from healthinsight.database.base import BaseModel

if TYPE_CHECKING:
    from .user import User


# pylint: disable=too-few-public-methods
class ProgressPhoto(BaseModel):
    """Represents a user's progress photo."""

    __tablename__ = "progress_photos"

    __table_args__ = (
        CheckConstraint(
            "length(trim(file_path)) > 0",
            name="ck_photo_file_path_not_empty",
        ),
        UniqueConstraint(
            "user_id",
            "file_path",
            name="uq_photo_user_file_path",
        ),
        Index(
            "ix_photo_user_id",
            "user_id",
        ),
        Index(
            "ix_photo_user_date",
            "user_id",
            "date",
        ),
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )
    date: Mapped[datetime.date] = mapped_column(nullable=False)
    file_path: Mapped[str] = mapped_column(nullable=False)
    notes: Mapped[str | None] = mapped_column()

    user: Mapped["User"] = relationship(
        back_populates="progress_photos",
    )

    def __repr__(self):
        return f"ProgressPhoto(id={self.id}, date={self.date!r})"
