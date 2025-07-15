from annotated_types import Interval
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.dialects.postgresql import JSONB, INTERVAL
from sqlalchemy.orm import relationship
from datetime import datetime
from .associations import courier_districts

from app.core.database import Base


class Courier(Base):
    __tablename__ = 'couriers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    active_order = Column(JSONB, nullable=True)
    avg_order_complete_time = Column(INTERVAL, default=0.0)
    avg_day_orders = Column(Float)

    register_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship('Order', back_populates='courier')
    districts = relationship("District",
                             secondary=courier_districts,
                             back_populates="couriers",
                             lazy='selectin'
    )

    def __repr__(self):
        return f"Курьер {self.name}"


