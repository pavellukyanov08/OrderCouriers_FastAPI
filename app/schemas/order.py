from pydantic import BaseModel

from app.models.order import OrderStatus
from app.schemas.district import DistrictBase


class OrderBase(BaseModel):
    name: str

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    name: str
    district: str


class OrderResponse(BaseModel):
    courier_id: int
    status: int
    district: int

    class Config:
        from_attributes = True


class OrderCreateResponse(BaseModel):
    order_id: int
    courier_id: int