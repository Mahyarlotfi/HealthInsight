"""Helper functions for tests."""

from sqlalchemy import inspect


def column_exists(engine, table_name, column_name):
    """Return True if a column exists."""
    inspector = inspect(engine)

    return any(
        column["name"] == column_name for column in inspector.get_columns(table_name)
    )
