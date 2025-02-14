from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .associations import courier_districts

from app.core.database import Base


class Courier(Base):
    __tablename__ = 'couriers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    district = Column(JSON, nullable=False)
    active_order = Column(JSON, nullable=True)
    avg_order_complete_time = Column(Float, default=0.0)
    avg_day_orders = Column(Integer, default=0)

    register_at = Column(DateTime, default=datetime.utcnow)

    districts = relationship("District", secondary=courier_districts, back_populates="couriers")

    def __repr__(self):
        return f"Курьер {self.name}"


