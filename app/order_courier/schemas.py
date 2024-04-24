from pydantic import BaseModel, constr
from typing import List, Optional
from datetime import datetime


class Districts(BaseModel):
    district: str


class Couriers(BaseModel):
    name: str
    district: int
    avg_order_complete_time: Optional[datetime]
    avg_day_orders: Optional[int] = 0


class Orders(BaseModel):
    name: str
    district: int
    status: int
    courier_id: int

    created_at: datetime
