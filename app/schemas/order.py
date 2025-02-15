from pydantic import BaseModel
from typing import List


class OrderCreate(BaseModel):
    name: str
    district: str


class OrderCompleted(BaseModel):
    id: int
    status: int
    courier_id: int

    class Config:
        orm_mode = True