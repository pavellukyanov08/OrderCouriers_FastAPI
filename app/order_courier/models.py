from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, DateTime, TIMESTAMP, JSON, func
from sqlalchemy.orm import relationship, declarative_base, DeclarativeBase

Base = declarative_base()
metadata = MetaData()


# class Order(Base):
#     __tablename__ = 'orders'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(100), nullable=False)
#     registered_at = Column(TIMESTAMP, default=func.now())
#
#     courier_id = Column(Integer, ForeignKey('couriers.id'))
#     district_id = Column(Integer, ForeignKey('districts.id'))
#     status_id = Column(Integer, ForeignKey('order_status.id'))
#
#
# class Courier(Base):
#     __tablename__ = 'couriers'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(100), nullable=False)
#     avg_order_complete_time = Column(DateTime)
#     avg_day_orders = Column(Integer)
#     active_order = Column(JSON)
#
#     district_id = Column(Integer, ForeignKey("district.id"))
#     order_id = Column(Integer, ForeignKey("order_status.id"))
#
#     # courier_users_relationship=relationship("user", back_populates="couriers.id")
#     courier_order_relationship=relationship("Order", back_populates="couriers.id")
#
#
# class District(Base):
#     __tablename__ = 'districts'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(100), nullable=False)
#
#
# class OrderStatus(Base):
#     __tablename__ = 'order_status'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     status = Column(String(10), nullable=False)
#
#     orderstatus_order = relationship("Order", back_populates="order_status")

order_status = Table(
    "order_status",
    metadata,

    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("status", String(10), nullable=False),

    # orderstatus_order=relationship("Order", back_populates="order_status"),
)

district = Table(
    "district",
    metadata,

    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=False),
)

courier = Table(
    "courier",
    metadata,

    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=False),
    Column("avg_order_complete_time", DateTime),
    Column("avg_day_orders", Integer),
    Column("active_order", JSON),

    # Связь с заказами и районами
    Column("district", Integer, ForeignKey(district.c.id)),
    Column("order", Integer, ForeignKey(order_status.c.id)),

    # courier_users_relationship=relationship("user", back_populates="courier"),
    # courier_order_relationship=relationship("order", back_populates="courier"),
)

order = Table(
    "order",
    metadata,

    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=False),
    Column("registered_at", TIMESTAMP, default=func.now()),
    Column("courier", Integer, ForeignKey(courier.c.id)),
    Column("district", Integer, ForeignKey(district.c.id)),
    Column("status", Integer, ForeignKey(order_status.c.id))
)

courier_order_relationship = relationship("order", back_populates="courier")

district_order_relationship = relationship('order', back_populates='district')

order_status_order_relationship = relationship('order', back_populates='order_status')







