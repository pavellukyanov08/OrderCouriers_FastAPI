from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, DateTime, TIMESTAMP, JSON, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()
metadata = MetaData()

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
    Column("district_id", Integer, ForeignKey(district.c.id)),
    Column("order_id", Integer, ForeignKey(order_status.c.id)),

    # courier_users_relationship=relationship("user", back_populates="courier"),
    # courier_order_relationship=relationship("order", back_populates="courier"),
)

order = Table(
    "order",
    metadata,

    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=False),
    Column("status", Integer, default=1),
    Column("registered_at", TIMESTAMP, default=func.now()),
    Column("courier_id", Integer, ForeignKey(courier.c.id)),
    Column("district_id", Integer, ForeignKey(district.c.id)),
    Column("status_id", Integer, ForeignKey(order_status.c.id))
)

# courier_order_relationship = relationship("order", back_populates="courier")
#
# district_order_relationship = relationship('order', back_populates='district')
#
# order_status_order_relationship = relationship('order', back_populates='order_status')
#
# courier_user_relationship = relationship('user', back_populates='courier')
