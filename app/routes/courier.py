from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models
from app.schemas.courier import *
from app.models import courier as courier_model, Courier
from app.core.database import get_db

courier_route = APIRouter()


@courier_route.post('/courier', response_model=CourierResponse)
def add_courier(courier: CourierCreate, db: Session = Depends(get_db)):
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
def get_courier(db:Session = Depends(get_db)):
    couriers = db.query(models.Courier).all()
    return couriers

