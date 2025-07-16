from datetime import timedelta

from sqlalchemy import select, func, cast, Date
from app.models.order import Order
from app.models.courier import Courier
from app.core.database import AsyncSessionLocal


async def get_courier_stats_by_orders(db: AsyncSessionLocal, courier_id: int):
    """
    Функиця подсчета среднего времени выполнения заказов и среднего количества заказов в день
    """
    result = await db.execute(select(Courier).where(Courier.id == courier_id))
    courier = result.scalar_one_or_none()

    # for courier in couriers:
    #     order_subq = (
    #         select(
    #             func.avg(Order.completed_time - Order.created_time).label('avg_order_complete_time'),
    #         )
    #         .where(
    #             Order.courier_id == courier.id,
    #             Order.completed_time.isnot(None)
    #         )
    #     )
    avg_time_query = (
        select(func.avg(Order.completed_time - Order.created_time))
        .where(Order.courier_id == courier.id, Order.completed_time.isnot(None))
    )
    avg_time_result = await db.execute(avg_time_query)
    avg_order_complete_time = avg_time_result.scalar()

    daily_count_subq = (
        select(
            cast(Order.completed_time, Date).label('day'),
            func.count(Order.id).label('daily_count')
        )
        .where(
            Order.courier_id == courier.id,
            Order.completed_time.isnot(None)
        )
        .group_by('day')
        .subquery()
    )
    avg_orders_query = select(func.avg(daily_count_subq.c.daily_count))
    avg_orders_result = await db.execute(avg_orders_query)
    avg_day_orders = avg_orders_result.scalar()

    # courier.avg_order_complete_time = timedelta(minutes=round(avg_order_complete_time.total_seconds() / 60))
    courier.avg_order_complete_time = avg_order_complete_time
    courier.avg_day_orders = avg_day_orders
