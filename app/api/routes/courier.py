from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from typing import Optional

from sqlalchemy.orm import selectinload

from app.models import Order, District, courier_districts
from app.schemas.courier import CourierResponse, CourierRegister
from app.models.courier import Courier
from app.core.database import get_session, AsyncSessionLocal, SyncSessionLocal

router = APIRouter()


@router.get('/couriers', response_model=CourierResponse)
async def get_courier(courier: Optional[int] = None, db: AsyncSessionLocal = Depends(get_session)):
    if courier is not None:
        stmt = select(Courier).options(selectinload(Courier.districts)).where(Courier.id == courier)
        result = await db.execute(stmt)
        existing_courier = result.scalar_one_or_none()

        if not existing_courier:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Курьер не найден')

        return [courier]

    else:
        stmt = select(Courier).options(selectinload(Courier.districts))
        result = await db.execute(stmt)
        couriers = result.scalars().all()
        return couriers


@router.post('/couriers', response_model=CourierResponse)
async def add_courier(courier: CourierRegister, db: AsyncSessionLocal = Depends(get_session)):
    try:
        stmt = select(District).where(District.name.in_(courier.districts))
        result = await db.execute(stmt)
        districts = result.scalars().all()
        print(districts)

        if len(districts) != len(set(courier.districts)):
            raise HTTPException(status_code=400, detail="Некоторые районы не найдены")

        new_courier = Courier(
            name=courier.name,
            districts=districts,
        )

        db.add(new_courier)
        await db.commit()
        await db.refresh(new_courier)

        stmt = (
            select(Courier)
            .options(selectinload(Courier.districts))
            .where(Courier.id == new_courier.id)
        )
        result = await db.execute(stmt)
        courier_with_districts = result.scalar_one()

        return courier_with_districts

    except Exception as e:
        db.rollback()
        return f'Ошибка добавления {str(e)}'


# @router.post('/couriers')
