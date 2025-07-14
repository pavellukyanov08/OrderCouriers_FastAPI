from pydantic import BaseModel

from app.schemas.district import DistrictBase


class OrderBase(BaseModel):
    name: str

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    name: str
    district: str


class OrderCreateResponse(BaseModel):
    order_id: int
    courier_id: int


class OrderCompletedResponse(BaseModel):
    order_id: int
    courier_id: int
    status: int
