from fastapi import APIRouter

from endpoints import product_groups, products, to_parses

api = APIRouter(prefix="/api/v1")

all_api_routers = [
    product_groups.router,
    to_parses.router,
    products.router,
]

for router in all_api_routers:
    api.include_router(router)
