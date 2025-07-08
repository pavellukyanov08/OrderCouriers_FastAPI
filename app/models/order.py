from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Float, DateTime
from datetime import datetime

from sqlalchemy.orm import relationship

from app.core.database import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    district = Column(JSON, nullable=False)
    status = Column(Integer, default=1)

    created_time = Column(DateTime, default=datetime.utcnow)
    completed_time = Column(DateTime, nullable=True)

    courier_id = Column(Integer, ForeignKey('couriers.id'))
    courier = relationship('Courier', back_populates='orders')



    def __repr__(self):
        return f"Заказ №{self.id}, район {self.district}"


