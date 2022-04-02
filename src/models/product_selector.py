from pydantic import BaseModel, validator


class BaseProductSelector(BaseModel):
    views_min: int = 0
    views_max: int | None
    product_on_sale_min: int = 0
    product_on_sale_max: int | None
    product_sold_min: int = 0
    product_sold_max: int | None
    is_company: bool | None
    has_phone: bool | None
    is_delivery: bool | None
    category: list[int] = list()
    subcategory: list[int] = list()
    price_min: int = 0
    price_max: int | None
    owner_reg_date: int | None
    time_delta: int | None = 24
    search: str | None
    city_search: str | None
    limit_rows: int = 100

    class Config:
        schema_extra = {
            "example": {
                "views_min": 0,
                "product_on_sale_min": 0,
                "product_sold_min": 0,
                "price_min": 0,
                "time_delta": 24,
                "limit_rows": 100,
            }
        }

    @validator("limit_rows")
    def name_must_contain_space(cls, v):
        max_value: int = 2000
        if v > max_value:
            raise ValueError(f"limit_rows cannot be greater than {max_value}")
        return v


class ProductSelector(BaseProductSelector):
    pass
