from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy import Integer
from app.core.database import Base


courier_districts = Table(
    "courier_districts",
    Base.metadata,
    Column("courier_id", Integer, ForeignKey("couriers.id"), primary_key=True),
    Column("district_id", Integer, ForeignKey("districts.id"), primary_key=True),
)
