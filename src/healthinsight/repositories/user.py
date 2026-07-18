"""Repository for User model."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from healthinsight.models.user import User
from healthinsight.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    """Repository for User-specific database operations."""

    def __init__(self, session: Session) -> None:
        """Initialize the repository."""
        super().__init__(session, User)

    def get_by_full_name(self, full_name: str) -> list[User]:
        """Return all users with the given full name."""
        statement = select(User).where(User.full_name == full_name)
        return list(self._session.scalars(statement))
