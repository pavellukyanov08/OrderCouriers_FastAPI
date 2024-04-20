from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from ..settings import TEMPLATES_DIRECTORY

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory=TEMPLATES_DIRECTORY)


@router.get("/")
def get_index_page(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})