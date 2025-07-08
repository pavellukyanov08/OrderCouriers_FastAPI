from pydantic import BaseModel
from typing import Optional


class OrderCreate(BaseModel):
    name: str
    district: str


class OrderResult(BaseModel):
    oder_id: int
    courier_id: int


class OrderStatus(BaseModel):
    courier_id: int
    status: str