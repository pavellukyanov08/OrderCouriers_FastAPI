from fastapi import APIRouter, Depends

from app import models
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


@courier_route.get('/courier', response_model=list[CourierResponse])
def get_courier(db: AsyncSessionLocal = Depends(get_session)):
    couriers = db.query(models.Courier).all()
    return couriers

