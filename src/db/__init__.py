from .base import engine, metadata
from .product_groups import pgroup
from .products import product

metadata.create_all(bind=engine)
