from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship
from database import Base


class Courier(Base):
    __tablename__ = "couriers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    avg_order_complete_time = Column(DateTime)
    avg_day_orders = Column(Integer)

    # Связь с заказами и районами
    order = Column(ForeignKey("orders.id"), nullable=False)


    def __repr__(self):
        return f"Курьер: {self.name} ({self.id})"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, nullable=False)
    status = Column(Integer, default=1)

    # Связь с курьерами и районами
    courier = relationship("Courier", back_populates="orders")
    district = relationship("District", back_populates="orders")

    def __repr__(self):
        return (f"Заказ №: {self.id}, Наименование: {self.name}\n"
                f"Курьер: {self.courier}, Имя: {self.name}")


class District(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, unique=True, nullable=False)

    # Связи с курьерами и заказами
    orders = Column(Integer, ForeignKey("orders.id"), nullable=False)

    def __repr__(self):
        return f"Район {self.name}, № {self.id}"
