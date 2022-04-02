import sqlalchemy
from sqlalchemy.sql import func

from .base import metadata

toparse = sqlalchemy.Table(
    "ToParse",
    metadata,
    sqlalchemy.Column("product_id", sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column(
        "is_was_parsed",
        sqlalchemy.Boolean,
        nullable=False,
        default=False,
        server_default="0",
    ),
    sqlalchemy.Column(
        "create",
        sqlalchemy.DateTime(timezone=False),
        default=func.now(),
        nullable=False,
        server_default=func.now(),
    ),
)
