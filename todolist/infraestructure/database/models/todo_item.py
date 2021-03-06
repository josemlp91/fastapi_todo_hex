from sqlalchemy.schema import CheckConstraint, Column, Table
from sqlalchemy.types import Boolean, Integer, String

from todolist.infraestructure.database.sqlalchemy import metadata

TodoItem = Table(
    "todo_item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("msg", String(length=100, collation='utf8_unicode_ci'), nullable=False, ),
    Column("is_done", Boolean(), nullable=False),
    Column("enable", Boolean(), nullable=False)
)
