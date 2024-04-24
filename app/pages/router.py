from typing import List

from fastapi import APIRouter, Request, Depends, Body, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_async_session
# from ..auth.models import user, User
# from ..database import SessionLocal
# from sqlalchemy.orm import Session
# from ..order_courier.schemas import Couriers as CourierScheme
from ..order_courier.schemas import Couriers, Orders
# from ..order_courier.models import Courier as CourierModel
from ..order_courier.models import courier, order

from ..settings import TEMPLATES_DIRECTORY

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory=TEMPLATES_DIRECTORY)


@router.get("/courier")
async def get_all_courier(session: AsyncSession = Depends(get_async_session)):
    """
        Получение всех курьеров системы

        Args:
            session (AsyncSession): Сессия базы данных.

        Returns:
            Словарь курьеров [type]: [description]
    """
    query = select(courier)
    result = await session.execute(query)
    couriers  = result.fetchall()

    couriers_data = [{"id": row[0], "name": row[1], "district": row[2], "order": row[3], "active_order": row[4],
                      "avg_order_complete_time": row[5], "avg_day_orders": row[6]} for row in couriers]
    return couriers_data
    # return templates.TemplateResponse("main_page.html", {"request": request, "couriers": result})


@router.get("/courier/{courier_id}")
async def get_courier(courier_id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Получение конкретного курьера по ID

        Args:
            courier_id (int): Идентификатор курьера.
            session (AsyncSession): Сессия базы данных.

        Returns:
            Словарь с данными по курьеру [type]: [description]
    """
    query = select(courier.c.id, courier.c.name, courier.c.district, courier.c.order, courier.c.active_order).where(courier.c.id == courier_id)
    result = await session.execute(query)
    couriers = result.all()

    couriers_data = [{"id": row[0], "name": row[1], "district": row[2], "order": row[3], "active_order": row[4]} for row in couriers]
    return couriers_data
    # return templates.TemplateResponse("main_page.html", {"request": request, "couriers": result})


@router.get("/order/{order_id}")
async def get_order(order_id: int, session: AsyncSession = Depends(get_async_session)):
    """
        Получение конкретного заказа по ID

        Args:
            order_id (int): Идентификатор заказа
            session (AsyncSession): Сессия базы данных.

        Returns:
            Словарь с данными по заказу [type]: [description]
    """
    query = (select(order.c.id, order.c.status, order.c.courier).where(order.c.id == order_id))
    result = await session.execute(query)
    order_data = result.fetchone()

    order_id, order_status, order_district = order_data
    order_info = {"id": order_id, "status": order_status, "district": order_district}
    return order_info


@router.post("/courier")
async def add_courier(new_courier: Couriers, session: AsyncSession = Depends(get_async_session)):
    """
        Добавление курьера в систему

        Args:
            new_courier (Couriers): Данные о новом курьере.
            session (AsyncSession): Сессия базы данных.

        Returns:
            Сообщение об успешном добавлении в систему
    """
    stmt = insert(courier).values(name=new_courier.name, district=new_courier.district)
    await session.execute(stmt)
    await session.commit()
    return {"message": f"Курьер {new_courier.name} был успешно добавлен"}


@router.post("/order")
async def add_order(new_order: Orders, session: AsyncSession = Depends(get_async_session)):
    """
        Добавление курьера в систему

        Args:
            new_order (Orders): Данные о новом курьере.
            session (AsyncSession): Сессия базы данных.

        Returns:
            Сообщение об успешном добавлении в систему
    """
    stmt = insert(order).values(name=new_order.name, district=new_order.district, status=new_order.status)
    await session.execute(stmt)
    await session.commit()
    return {"message": f"Курьер {new_order.name} был успешно добавлен"}

# @router.get("/")
# async def get_all_couriers_page(request: Request, session: AsyncSession = Depends(get_db())):
#     query = select(courier)
#     result = await session.execute(query)
#     return templates.TemplateResponse("main_page.html", {"request": request, "couriers": result})


# @router.get("/registr_courier")
# async def registr_courier(request: Request):
#     return templates.TemplateResponse("registr_courier.html", {"request": request})
#
#
# @router.post("/create_courier")
# async def create_courier(couriers: courier, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(couriers).values(**couriers.dict())
#     await session.execute(stmt)
#     return templates.TemplateResponse("registr_courier.html",
#                                       {"request": Request,
#                                        "message": "Курьер успешно зарегистрирован"})
