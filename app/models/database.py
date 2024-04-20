#
#
# metadata = MetaData()
#
# couriers = Table(
#     "couriers",
#     metadata,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("name", String(100), nullable=False),
#     Column("avg_order_complete_time", DateTime),
#     Column("avg_day_orders", Integer),
#
#     # Связь с заказами и районами
#     Column("order_id", Integer, ForeignKey("orders.id"))
# )
#
# orders = Table(
#     "orders",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(100), nullable=False),
#     Column("status", Integer, default=1),
# )
#
# districts = Table(
#     "districts",
#
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(100), nullable=False),
#
#     # Связи с курьерами и заказами
#     Column("order_id", Integer, ForeignKey("orders.id")),
# )
