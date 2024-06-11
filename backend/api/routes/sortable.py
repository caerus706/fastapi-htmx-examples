from typing import Optional
from fastapi import APIRouter, Header
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("sortable/index.html", context)

@router.post("/items")
def items(request: Request):
    return ""