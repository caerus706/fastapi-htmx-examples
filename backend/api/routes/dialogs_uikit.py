from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("dialogs_uikit/index.html", context)

@router.get("/modal", response_class=HTMLResponse)
def modal(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("dialogs_uikit/modal.html", context)