from datetime import datetime
from typing import List, Optional
from .district import DistrictBase
from pydantic import BaseModel


class CourierResponse(BaseModel):
    id: Optional[int] = None
    name: str
    active_order: Optional[int] = None
    avg_order_complete_time: Optional[float] = None
    avg_day_orders: Optional[int] = None
    districts: List[DistrictBase] = []

    model_config = {
        'from_attributes': True
    }


class CourierRegister(BaseModel):
    name: str
    districts: List[str]


class CourierRegisterResponse(BaseModel):
    id: int
    name: str
    districts: List[DistrictBase]

