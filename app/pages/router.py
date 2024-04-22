from typing import List

from fastapi import APIRouter, Request, Depends
from fastapi import Form
from fastapi.templating import Jinja2Templates
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from ..auth.models import user, User
from ..database import get_async_session
from ..order_courier.schemas import Couriers, Orders
from ..order_courier.models import courier

from ..settings import TEMPLATES_DIRECTORY

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory=TEMPLATES_DIRECTORY)


@router.get("/")
async def get_all_couriers_page(request: Request, session: AsyncSession = Depends(get_async_session)):
    query = select(courier)
    result = await session.execute(query)
    return templates.TemplateResponse("main_page.html", {"request": request, "couriers": result})


@router.post("/registr_courier")
async def register_courier(new_courier: Couriers, request: Request, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(courier).values(**new_courier.dict())
    await session.execute(stmt)
    return templates.TemplateResponse("registr_courier.html",
                                      {"request": request,
                                       "message": "Курьер успешно зарегистрирован"})


# @router.post("/registr_order")
# async def register_courier(new_order: Orders, request: Request, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(courier).values(**new_courier.dict())
#     await session.execute(stmt)
#     return templates.TemplateResponse("registr_order.html",
#                                       {"request": request,
#                                        "message": "Курьер успешно зарегистрирован"})
