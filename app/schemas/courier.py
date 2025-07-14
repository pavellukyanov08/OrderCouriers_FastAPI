from datetime import datetime
from typing import List, Optional
from .district import DistrictBase
from pydantic import BaseModel


class CourierRegister(BaseModel):
    name: str
    districts: List[str]


class CourierBase(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class CourierResponse(BaseModel):
    id: int
    name: str
    districts: List[DistrictBase]
    active_order: Optional[str]
    avg_order_complete_time: Optional[datetime]
    avg_day_orders: int

