from fastapi import FastAPI
from app.routes.courier import courier_route


def create_app():
    app = FastAPI(
        title="Сервис распределения заказов по курьерам"
    )

    @app.get('/')
    async def root():
        return {'message': 'Order courier service'}

    app.include_router(courier_route)

    return app