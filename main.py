import uvicorn
from fastapi import FastAPI
from app.routes import courier
from app.routes.courier import courier_route

app = FastAPI(
    title="Сервис распределения заказов по курьерам"
)


app.include_router(courier_route)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)

