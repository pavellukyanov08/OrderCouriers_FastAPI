from datetime import timedelta
from typing import List, Optional
from .district import DistrictRead
from pydantic import BaseModel, ConfigDict


def serialize_timedelta(td: timedelta) -> int:
   return round(td.total_seconds() / 60)


class CourierBase(BaseModel):
    id: int
    name: str

    model_config = {'from_attributes': True}


class CourierRead(CourierBase):
    active_order: Optional[dict] = None
    avg_order_complete_time: Optional[timedelta] = None
    avg_day_orders: Optional[float] = None
    districts: List[DistrictRead]

    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            timedelta: serialize_timedelta,
        }
    )


class CourierRegister(BaseModel):
    name: str
    districts: List[str]


class CourierRegisterResponse(BaseModel):
    id: int
    name: str
    districts: List[DistrictRead]

