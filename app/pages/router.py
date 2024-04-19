from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import os

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates_dir")


@router.get("/")
def get_base_page(request: Request):
    return templates.TemplateResponse("templates/index.html", {"request": request})