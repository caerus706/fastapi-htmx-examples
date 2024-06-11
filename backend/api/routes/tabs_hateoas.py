from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("tabs_hateoas/index.html", context)


@router.get("/tab1", response_class=HTMLResponse)
def tab1(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("tabs_hateoas/tab1.html", context)


@router.get("/tab2", response_class=HTMLResponse)
def tab2(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("tabs_hateoas/tab2.html", context)


@router.get("/tab3", response_class=HTMLResponse)
def tab3(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("tabs_hateoas/tab3.html", context)
