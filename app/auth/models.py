from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP, Boolean, func, Table, MetaData, DateTime, JSON
from sqlalchemy.orm import declarative_base

from ..order_courier.models import courier

Base = declarative_base()
metadata = MetaData()


user = Table(
    "user",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("email", String(100), nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime),
    Column("hashed_password", String, nullable=True),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),

    Column("courier_id", Integer, ForeignKey(courier.c.id)),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    registered_at = Column(TIMESTAMP(timezone=True), default=func.now())
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)

    Column("courier_id", Integer, ForeignKey(courier.c.id)),
