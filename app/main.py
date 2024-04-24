from fastapi import FastAPI
from sqlalchemy import event, select
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

# from .auth.auth import auth_backend, fastapi_users
# from .auth.schemas import UserRead, UserCreate
from .settings import STATIC_DIRECTORY
from .pages.router import router as router_pages

app = FastAPI(
    title="Сервис распределения заказов по курьерам"
)

# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth/jwt",
#     tags=["Auth"],
# )
#
# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["Auth"],
# )

# origins = [
#     "http://localhost:8000",
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "PUT"],
#     allow_headers=["Content-Type", "Authorization", "Access-Control-Request-Headers", "Set-Cookie", "Access-Control-Allow-Headers"],
# )


app.include_router(router_pages)
app.mount("/static", StaticFiles(directory=STATIC_DIRECTORY), name="static")

