from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Float, DateTime
from sqlalchemy.orm import relationship
from .associations import courier_districts

from app.core.database import Base


class District(Base):
    __tablename__ = 'districts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    couriers = relationship("Courier", secondary=courier_districts, back_populates="districts")


    def __repr__(self):
        return f"Район {self.name}"


