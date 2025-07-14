from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .associations import courier_districts

from app.core.database import Base


class Courier(Base):
    __tablename__ = 'couriers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    active_order = Column(Integer, ForeignKey('orders.id'), nullable=True)
    avg_order_complete_time = Column(Float, default=0.0)
    avg_day_orders = Column(Integer, default=0)

    register_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship('Order', back_populates='courier', foreign_keys='Order.courier_id')
    districts = relationship("District",
                             secondary=courier_districts,
                             back_populates="couriers",
                             lazy='selectin'
    )

    def __repr__(self):
        return f"Курьер {self.name}"


