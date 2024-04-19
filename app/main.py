from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from settings import TEMPLATES_DIRECTORY

app = FastAPI()

templates = Jinja2Templates(directory=TEMPLATES_DIRECTORY)


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})