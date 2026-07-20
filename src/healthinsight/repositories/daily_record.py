"""Repository for DailyRecord model."""

import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from healthinsight.models.daily_record import DailyRecord
from healthinsight.repositories.base import BaseRepository


class DailyRecordRepository(BaseRepository[DailyRecord]):
    """Repository for DailyRecord-specific database operations."""

    def __init__(self, session: Session) -> None:
        """Initialize the repository."""
        super().__init__(session, DailyRecord)

    def get_by_user(self, user_id: int) -> list[DailyRecord]:
        """Return all records for a user."""
        statement = (
            select(DailyRecord)
            .where(DailyRecord.user_id == user_id)
            .order_by(DailyRecord.date)
        )
        return list(self._session.scalars(statement))

    def get_by_date(
        self,
        record_date: datetime.date,
    ) -> list[DailyRecord]:
        """Return all records for a specific date."""
        statement = select(DailyRecord).where(
            DailyRecord.date == record_date,
        )
        return list(self._session.scalars(statement))

    def get_by_date_range(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
    ) -> list[DailyRecord]:
        """Return all records within a date range."""
        statement = (
            select(DailyRecord)
            .where(
                DailyRecord.date.between(
                    start_date,
                    end_date,
                )
            )
            .order_by(DailyRecord.date)
        )
        return list(self._session.scalars(statement))
