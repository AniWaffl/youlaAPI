import datetime

from pydantic import BaseModel

from core.utils import get_datetime


class BaseProduct(BaseModel):
    id: str
    name: str
    price: int
    discounted_price: int
    date_created: datetime.datetime
    category: int
    subcategory: int
    url_branch: str = f"https://youla.ru/p{id}f"
    latitude: float | None = None
    longitude: float | None = None
    description: str = ""
    views: int = 0
    delivery_available: bool = False
    phone: str | None
    owner_id: str
    owner_type: str
    owner_name: str
    owner_reg_date: datetime.datetime
    prods_active_cnt: int
    prods_sold_cnt: int


class Product(BaseProduct):
    create: datetime.datetime = get_datetime()


class ProductIn(BaseProduct):
    pass
