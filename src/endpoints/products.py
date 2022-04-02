from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger

from models import ProductSelector
from models.product import BaseProduct, Product, ProductIn
from repositories.products import ProductRepository

from .depends import get_product_repository

router = APIRouter(prefix="/products", tags=["products"])

not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Products not found"
)


@router.get("/{product_id}", response_model=Product)
async def read_products(
    product_id: str, product: ProductRepository = Depends(get_product_repository)
):
    return await product.get_by_id(id=product_id)


@router.get("/", response_model=list[Product])
async def read_products(
    limit: int = 100,
    skip: int = 0,
    product: ProductRepository = Depends(get_product_repository),
):
    return await product.get_all(limit=limit, skip=skip)


@router.get("/{product_id}", response_model=Product | None)
async def read_product(
    product_id: str, product: ProductRepository = Depends(get_product_repository)
):
    return await product.get_by_id(id=product_id) or not_found_exception


@router.post("/filter", response_model=list[Product])
async def filter_product(
    filter: ProductSelector,
    product: ProductRepository = Depends(get_product_repository),
):
    return await product.get_by_filters(filters=filter) or not_found_exception


@router.post("/", response_model=Product)
async def create_product(
    m: ProductIn, product: ProductRepository = Depends(get_product_repository)
):
    return await product.create(m=m)


@router.put("/{product_id}", response_model=Product)
async def update_product(
    product_id: str,
    m: ProductIn,
    product: ProductRepository = Depends(get_product_repository),
):
    pgroup = await product.get_by_id(id=product_id)
    if pgroup is None:
        raise not_found_exception
    return await product.update(id=product_id, m=m)


@router.delete("/{product_id}")
async def delete_product(
    product_id: str,
    product: ProductRepository = Depends(get_product_repository),
):
    pgroup = await product.get_by_id(id=product_id)
    if pgroup is None:
        raise not_found_exception
    await product.delete(id=product_id)
    return {"status": True}
