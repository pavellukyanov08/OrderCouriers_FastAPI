from enum import Enum

from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime

from fastapi import FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from .settings import STATIC_DIRECTORY
from .pages.router import router as router_pages

app = FastAPI(
    title="Cервис распределения заказов по курьерам"
)

# fake_couriers = [
#     {"id": 1, "name": "Michael", "districts": [{"id": 1, "district": ["Центральный", "Железнодорожный"]}],
#      "avg_order_complete_time": "10", "avg_day_orders": "5"},
#
#     {"id": 2, "name": "Dima", "district": ["Ленинский", "Железнодорожный"],
#      "avg_order_complete_time": "15", "avg_day_orders": "7"},
#
#     {"id": 3, "name": "Semen", "district": ["Октябрьский", "Центральный"],
#      "avg_order_complete_time": "20", "avg_day_orders": ""},
# ]

fake_couriers = [
    {"id": 1, "name": "Michael", "districts": [{"id": 1, "district": ["Центральный", "Железнодорожный"]}],
     "avg_order_complete_time": "10", "avg_day_orders": "5"},

    {"id": 2, "name": "Dima", "districts": [{"id": 2, "district": ["Ленинский", "Железнодорожный"]}],
     "avg_order_complete_time": "15", "avg_day_orders": "7"},

    {"id": 3, "name": "Semen", "districts": [{"id": 3, "district": ["Центральный", "Ленинский"]}],
     "avg_order_complete_time": "15", "avg_day_orders": "8"},
]


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


# @app.post("/couriers")
# def create_couriers(couriers: List[Couriers]):
#     fake_couriers.extend(couriers)
#     return {"status": 200, "data": fake_couriers}


# @app.post("/couriers/{courier_id}")
# def change_user_name(courier_id: int, new_name: str):
#     current_courier = list(filter(lambda courier: courier.get("id") == courier_id, fake_couriers2))[0]
#     current_courier["name"] = new_name
#     return {"status": 200, "data": current_courier}


@app.get("/couriers/{courier_id}", response_model=List[Couriers])
def get_couriers(courier_id: int):
    return [courier for courier in fake_couriers if courier.get("id") == courier_id]

# app.mount("/static", StaticFiles(directory=STATIC_DIRECTORY), name="static")
# app.include_router(router_pages)
