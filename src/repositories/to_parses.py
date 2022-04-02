from core.utils import get_datetime
from db.to_parse import toparse
from models import BaseToParse, ToParse, ToParseIn

from .base import BaseRepository

db_model = toparse
Model, ModelIn, BaseModel = ToParse, ToParseIn, BaseToParse


class ToParseRepository(BaseRepository):
    async def create(self, *, m: ModelIn) -> Model:
        m = Model(
            product_id=m.product_id,
            is_was_parsed=m.is_was_parsed,
            create=get_datetime(),
        )
        values = {**m.dict()}
        query = db_model.insert().values(**values)
        await self.database.execute(query=query)
        return m

    async def update(self, product_id: str, m: ModelIn) -> Model:
        m = Model(
            product_id=m.product_id,
            is_was_parsed=m.is_was_parsed,
            create=get_datetime(),
        )
        values = {**m.dict()}
        query = (
            db_model.update()
            .where(db_model.c.product_id == product_id)
            .values(**values)
        )
        await self.database.execute(query=query)
        return m

    async def get_all(self, limit: int = 100, skip: int = 0) -> list[Model]:
        query = db_model.select().limit(limit).offset(skip)
        rows = await self.database.fetch_all(query=query)
        return [Model.parse_obj(m) for m in rows] or list()

    async def delete(self, product_id: str):
        query = db_model.delete().where(db_model.c.product_id == product_id)
        return await self.database.execute(query=query)

    async def get_by_id(self, product_id: str) -> Model | None:
        query = db_model.select().where(db_model.c.product_id == product_id)
        m = await self.database.fetch_one(query=query)
        if m is None:
            return None
        return Model.parse_obj(m)


__all__ = ["ToParseRepository"]
