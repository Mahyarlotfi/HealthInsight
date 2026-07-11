"""SQLAlchemy User model."""

from datetime import date

from sqlalchemy.orm import Mapped, mapped_column

from healthinsight.database.base import BaseModel


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

    def __repr__(self):
        return f"User(id={self.id}, full_name={self.full_name!r})"
