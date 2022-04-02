from core.utils import get_datetime
from db.product_groups import pgroup
from models import BasePGroup, PGroup, PGroupIn

from .base import BaseRepository

db_model = pgroup
Model, ModelIn, BaseModel = PGroup, PGroupIn, BasePGroup


class PGroupRepository(BaseRepository):
    async def create(self, *, m: ModelIn) -> Model:
        m = Model(href=m.href, is_active=m.is_active, update=get_datetime())
        values = {**m.dict()}
        query = db_model.insert().values(**values)
        await self.database.execute(query=query)
        return m

    async def update(self, href: str, m: ModelIn) -> Model:
        m = Model(href=m.href, is_active=m.is_active, update=get_datetime())
        values = {**m.dict()}
        query = db_model.update().where(db_model.c.href == href).values(**values)
        await self.database.execute(query=query)
        return m

    async def get_all(self, limit: int = 100, skip: int = 0) -> list[Model]:
        query = db_model.select().limit(limit).offset(skip)
        rows = await self.database.fetch_all(query=query)
        return [Model.parse_obj(m) for m in rows] or list()

    async def delete(self, href: str):
        query = db_model.delete().where(db_model.c.href == href)
        return await self.database.execute(query=query)

    async def get_by_id(self, href: str) -> Model | None:
        query = db_model.select().where(db_model.c.href == href)
        m = await self.database.fetch_one(query=query)
        if m is None:
            return None
        return Model.parse_obj(m)


__all__ = ["PGroupRepository"]
