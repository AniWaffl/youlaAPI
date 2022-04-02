from db.base import database
from repositories.product_groups import PGroupRepository
from repositories.products import ProductRepository
from repositories.to_parses import ToParseRepository


def get_pgroup_repository() -> PGroupRepository:
    return PGroupRepository(database)


def get_toparse_repository() -> ToParseRepository:
    return ToParseRepository(database)


def get_product_repository() -> ProductRepository:
    return ProductRepository(database)
