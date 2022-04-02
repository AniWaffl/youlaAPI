from fastapi import APIRouter, Depends, HTTPException, status

from models.to_parse import BaseToParse, ToParse, ToParseIn
from repositories.to_parses import ToParseRepository

from .depends import get_toparse_repository

router = APIRouter(prefix="/to_parses", tags=["to_parses"])

not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
)


@router.get("/", response_model=list[ToParse])
async def read_to_parses(
    limit: int = 100,
    skip: int = 0,
    to_parses: ToParseRepository = Depends(get_toparse_repository),
):
    return await to_parses.get_all(limit=limit, skip=skip)


@router.get("/{product_id}", response_model=ToParse | None)
async def read_ToParse(
    product_id: str, to_parses: ToParseRepository = Depends(get_toparse_repository)
):
    return await to_parses.get_by_id(product_id=product_id)


@router.post("/", response_model=ToParse)
async def create_to_parses(
    m: ToParseIn, to_parses: ToParseRepository = Depends(get_toparse_repository)
):
    return await to_parses.create(m=m)


@router.put("/{product_id}", response_model=ToParse)
async def update_to_parses(
    product_id: str,
    m: ToParseIn,
    to_parses: ToParseRepository = Depends(get_toparse_repository),
):
    ToParse = await to_parses.get_by_id(product_id=product_id)
    if ToParse is None:
        raise not_found_exception
    return await to_parses.update(product_id=product_id, m=m)


@router.delete("/{product_id}")
async def delete_to_parses(
    product_id: str,
    to_parses: ToParseRepository = Depends(get_toparse_repository),
):
    ToParse = await to_parses.get_by_id(product_id=product_id)
    if ToParse is None:
        raise not_found_exception
    result = await to_parses.delete(product_id=product_id)
    return {"status": True}
