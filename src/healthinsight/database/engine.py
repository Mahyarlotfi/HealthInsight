"""Database engine configuration."""

from sqlalchemy import create_engine

from healthinsight.config.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
