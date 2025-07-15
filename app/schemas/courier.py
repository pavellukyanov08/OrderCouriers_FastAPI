from datetime import timedelta
from typing import List, Optional
from .district import DistrictResponse
from pydantic import BaseModel


class CourierResponse(BaseModel):
    id: int
    name: str
    active_order: Optional[dict] = None
    avg_order_complete_time: Optional[timedelta] = None
    avg_day_orders: Optional[float] = None
    districts: List[DistrictResponse]

    model_config = {
        'from_attributes': True
    }


class CourierRegister(BaseModel):
    name: str
    districts: List[str]


class CourierRegisterResponse(BaseModel):
    id: int
    name: str
    districts: List[DistrictResponse]

