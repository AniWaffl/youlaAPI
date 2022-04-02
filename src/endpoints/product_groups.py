from fastapi import APIRouter, Depends, HTTPException, status

from models.product_group import PGroup, PGroupIn
from repositories.product_groups import PGroupRepository

from .depends import get_pgroup_repository

router = APIRouter(prefix="/pgroups", tags=["pgroups"])

not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Product group not found"
)


@router.get("/", response_model=list[PGroup])
async def read_pgroups(
    limit: int = 100,
    skip: int = 0,
    pgroups: PGroupRepository = Depends(get_pgroup_repository),
):
    return await pgroups.get_all(limit=limit, skip=skip)


@router.get("/{href}", response_model=PGroup | None)
async def read_pgroup(
    href: str, pgroups: PGroupRepository = Depends(get_pgroup_repository)
):
    return await pgroups.get_by_id(href=href)


@router.post("/", response_model=PGroup)
async def create_pgroups(
    m: PGroupIn, pgroups: PGroupRepository = Depends(get_pgroup_repository)
):
    return await pgroups.create(m=m)


@router.put("/{href}", response_model=PGroup)
async def update_pgroups(
    href: str, m: PGroupIn, pgroups: PGroupRepository = Depends(get_pgroup_repository)
):
    pgroup = await pgroups.get_by_id(href=href)
    if pgroup is None:
        raise not_found_exception
    return await pgroups.update(href=href, m=m)


@router.delete("/{href}")
async def delete_pgroups(
    href: int,
    pgroups: PGroupRepository = Depends(get_pgroup_repository),
):
    pgroup = await pgroups.get_by_id(href=href)
    if pgroup is None:
        raise not_found_exception
    result = await pgroups.delete(href=href)
    return {"status": True}
