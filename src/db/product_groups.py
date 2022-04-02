import datetime

import sqlalchemy
from sqlalchemy.sql import func

from .base import metadata

pgroup = sqlalchemy.Table(
    "pgroup",
    metadata,
    sqlalchemy.Column("href", sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column(
        "is_active",
        sqlalchemy.Boolean,
        nullable=False,
        default=True,
        server_default="1",
    ),
    sqlalchemy.Column(
        "update",
        sqlalchemy.DateTime(timezone=False),
        default=datetime.datetime.utcnow,
        nullable=False,
        onupdate=func.now(),
        server_onupdate=func.now(),
    ),
)
