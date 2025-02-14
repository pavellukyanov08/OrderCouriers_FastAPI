import uvicorn
from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title="Сервис распределения заказов по курьерам"
)


@app.get("/")
def main():
    return {"DB_HOST": settings.DB_HOST, "SECRET_KEY": settings.SECRET_KEY}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)

