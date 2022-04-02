import datetime

from pydantic import BaseModel

from core.utils import get_datetime


class BasePGroup(BaseModel):
    href: str
    is_active: bool = True


class PGroup(BasePGroup):
    update: datetime.datetime = get_datetime()


class PGroupIn(BasePGroup):
    pass
