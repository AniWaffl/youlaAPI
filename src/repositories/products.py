from datetime import datetime, timedelta

from loguru import logger
from sqlalchemy import and_, desc

from db.products import product
from models import BaseProduct, Product, ProductIn, ProductSelector

from .base import BaseRepository

db_model = product
Model, ModelIn, BaseModel = Product, ProductIn, BaseProduct


class ProductRepository(BaseRepository):
    async def create(self, *, m: ModelIn) -> Model:
        m = Model(**m.dict())
        values = {**m.dict()}
        query = db_model.insert().values(**values)
        await self.database.execute(query=query)
        return m

    async def update(self, id: str, m: ModelIn) -> Model:
        m = Model(**m.dict())
        values = {**m.dict()}
        query = db_model.update().where(db_model.c.id == id).values(**values)
        await self.database.execute(query=query)
        return m

    async def get_all(self, limit: int = 100, skip: int = 0) -> list[Model]:
        query = db_model.select().limit(limit).offset(skip)
        rows = await self.database.fetch_all(query=query)
        return [Model.parse_obj(m) for m in rows] or list()

    async def delete(self, id: str):
        query = db_model.delete().where(db_model.c.id == id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: str) -> Model | None:
        query = db_model.select().where(db_model.c.id == id)
        m = await self.database.fetch_one(query=query)
        if m is None:
            return None
        return Model.parse_obj(m)

    async def get_by_filters(self, filters: ProductSelector) -> list[Model]:
        logger.debug(filters)
        conditions = []
        if filters.views_min:
            conditions.append(db_model.c.views >= filters.views_min)
        if filters.views_max is not None:
            conditions.append(db_model.c.views <= filters.views_max)
        if filters.product_on_sale_min is not None:
            conditions.append(
                db_model.c.prods_active_cnt >= filters.product_on_sale_min
            )
        if filters.product_on_sale_max is not None:
            conditions.append(
                db_model.c.prods_active_cnt <= filters.product_on_sale_max
            )
        if filters.product_sold_min is not None:
            conditions.append(db_model.c.prods_sold_cnt >= filters.product_sold_min)
        if filters.product_sold_max is not None:
            conditions.append(db_model.c.prods_sold_cnt <= filters.product_sold_max)
        if filters.is_company is not None:
            if filters.is_company:
                conditions.append(db_model.c.owner_type != "person")
            else:
                conditions.append(db_model.c.owner_type == "person")
        if filters.has_phone is not None:
            if filters.has_phone:
                conditions.append(db_model.c.phone != None)
            else:
                conditions.append(db_model.c.phone == None)
        if filters.is_delivery is not None:
            if filters.is_delivery:
                conditions.append(db_model.c.delivery_available == True)
            else:
                conditions.append(db_model.c.delivery_available == False)
        if filters.category:
            conditions.append(db_model.c.category.in_(filters.category))
        if filters.subcategory:
            conditions.append(db_model.c.subcategory.in_(filters.subcategory))
        if filters.price_min is not None:
            conditions.append(db_model.c.price <= filters.price_min)
        if filters.price_max is not None:
            conditions.append(db_model.c.price >= filters.price_max)
        if filters.owner_reg_date is not None:
            conditions.append(
                db_model.c.owner_reg_date
                >= datetime.strptime(f"{filters.owner_reg_date}/01/01", "%Y/%m/%d")
            )
        if filters.time_delta is not None:
            since = datetime.utcnow() - timedelta(hours=filters.time_delta)
            conditions.append(db_model.c.date_created >= since)
        if filters.search is not None:
            conditions.append(db_model.c.name.ilike(f"%{filters.search}%"))
        if filters.city_search is not None:
            # TODO add search by city name -> to coords -> select
            pass
        query = (
            db_model.select()
            .where(and_(*conditions))
            .order_by(desc(db_model.c.date_created))
            .limit(filters.limit_rows)
        )
        m = await self.database.fetch_all(query=query)

        if m is None:
            raise ValueError(f"Products with filters <{filters}> not found")
        return [Model.parse_obj(dict(i)) for i in m]


__all__ = ["ProductRepository"]
