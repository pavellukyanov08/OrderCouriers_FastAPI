from fastapi import FastAPI
from app.api.routes import district, courier, order


def create_app():
    app = FastAPI(
        title="Сервис распределения заказов по курьерам"
    )

    @app.get('/')
    async def root():
        return {'message': 'Order courier service'}

    app.include_router(district.router)
    app.include_router(courier.router)
    app.include_router(order.router)

    return app