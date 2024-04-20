# from pydantic import BaseModel
# from typing import List, Optional
# from datetime import datetime
#
#
# class Couriers(BaseModel):
#     id: int
#     name: str
#     districts: List[str]
#     avg_order_complete_time: Optional[datetime]
#     avg_day_orders: Optional[int]
#
#
# class Orders(BaseModel):
#     id: int
#     name: str
#     districts: str
#     status: int
#     courier_id: Optional[int]
