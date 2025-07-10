from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from typing import Optional

from app import models
from app.models import Order
from app.schemas.courier import CourierBase, CourierResponse
from app.models.courier import Courier
from app.core.database import get_session, AsyncSessionLocal, SyncSessionLocal

courier_route = APIRouter()


@courier_route.post('/courier', response_model=CourierBase)
def add_courier(courier: CourierBase, db: SyncSessionLocal = Depends(get_session)):
    try:
        new_courier = models.Courier(
            name=courier.name,
            district=','.join(courier.districts)
        )

        db.add(new_courier)
        db.commit()
        db.refresh(new_courier)

        return new_courier

    except Exception as e:
        db.rollback()
        return f'Ошибка добавления {str(e)}'


@courier_route.get('/courier', response_model=CourierResponse)
async def get_courier(courier_id: Optional[int], db: AsyncSessionLocal = Depends(get_session)):
    if courier_id:
        stmt = (
            select(
                Courier,
                Order
            )
            .join(Order, Courier.id == Order.courier_id)
            .where(Courier.id == courier_id)
            .group_by(Courier.id, Order.id)
            .order_by(Courier.id)
        )
        result = await db.execute(stmt)
        courier = result.scalar_one_or_none()

        if not courier:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Курьер не найден')

        couriers = courier

    else:
        stmt = select(Courier).all()
        result = await db.execute(stmt)
        couriers = result.scalars().all()

    return [{
        'id': courier.id,
        'name': courier.name,
        'active_order': {
            'order_id': courier.active_order_id,
            'order_name': courier.active_order_name,
        },
    } for courier in couriers]
