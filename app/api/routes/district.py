from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from starlette import status

from app.models import District
from app.schemas.district import DistrictBase
from app.models.courier import Courier
from app.core.database import get_session, AsyncSessionLocal, SyncSessionLocal

router = APIRouter()


@router.post('/districts', response_model=DistrictBase, status_code=201)
async def add_district(district: DistrictBase, db: AsyncSessionLocal = Depends(get_session)):
    try:
        stmt = select(District).where(District.name == district.name)
        result = await db.execute(stmt)
        existing_district = result.scalars().first()

        if existing_district:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Район уже существует")

        new_district = District(
            name=district.name,
        )

        db.add(new_district)
        await db.commit()
        await db.refresh(new_district)

        return new_district

    except Exception as e:
        db.rollback()
        return f'Ошибка добавления {str(e)}'


@router.get('/couriers', response_model=DistrictBase)
async def get_districts(district: str, db: AsyncSessionLocal = Depends(get_session)):
    if district:
        stmt = select(District)
        result = await db.execute(stmt)
        courier = result.scalar().all()

        if not courier:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Курьер не найден')

        couriers = [courier]

    else:
        stmt = select(Courier)
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