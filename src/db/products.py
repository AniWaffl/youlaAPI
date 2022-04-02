import sqlalchemy
from sqlalchemy.sql import func

from .base import metadata

product = sqlalchemy.Table(
    "product",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("price", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("discounted_price", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column(
        "date_created", sqlalchemy.DateTime(timezone=True), nullable=False
    ),
    sqlalchemy.Column("category", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("subcategory", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("url_branch", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("latitude", sqlalchemy.Float, nullable=True),
    sqlalchemy.Column("longitude", sqlalchemy.Float, nullable=True),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("views", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("delivery_available", sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column("phone", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("owner_id", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("owner_type", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("owner_name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column(
        "owner_reg_date", sqlalchemy.DateTime(timezone=True), nullable=False
    ),
    sqlalchemy.Column("prods_active_cnt", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("prods_sold_cnt", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column(
        "create",
        sqlalchemy.DateTime(timezone=True),
        nullable=False,
        default=func.now(),
        server_default=func.now(),
    ),
)
