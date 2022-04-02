import datetime

from pydantic import BaseModel

from core.utils import get_datetime


class BaseToParse(BaseModel):
    product_id: str
    is_was_parsed: bool = False


class ToParse(BaseToParse):
    create: datetime.datetime = get_datetime()


class ToParseIn(BaseToParse):
    pass
