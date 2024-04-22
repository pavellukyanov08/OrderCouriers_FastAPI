from enum import Enum

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# fake_couriers = [
#     {"id": 1, "name": "Michael", "districts": [{"id": 1, "district": ["Центральный", "Железнодорожный"]}],
#      "avg_order_complete_time": "10", "avg_day_orders": "5"},
#
#     {"id": 2, "name": "Dima", "districts": [{"id": 2, "district": ["Ленинский", "Железнодорожный"]}],
#      "avg_order_complete_time": "15", "avg_day_orders": "7"},
#
#     {"id": 3, "name": "Semen", "districts": [{"id": 3, "district": ["Центральный", "Ленинский"]}],
#      "avg_order_complete_time": "15", "avg_day_orders": "8"},
# ]


class DistrictsName(Enum):
    leninsky = "Ленинский"
    railway = "Железнодорожный"
    industrial = "Индустриальный"
    oktyabrsky = "Октябрьский"
    central = "Центральный"


class Districts(BaseModel):
    id: int
    district: List[DistrictsName]


class Couriers(BaseModel):
    id: int
    name: str
    districts: List[Districts]
    avg_order_complete_time: Optional[datetime]
    avg_day_orders: Optional[int] = 0


class Orders(BaseModel):
    id: int
    name: str
    districts: str
    status: int
    courier_id: int

    created_at: datetime
