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
    return templates.TemplateResponse("dialogs_browser/index.html", context)

@router.post("/submit")
def graph(request: Request, hx_prompt: Optional[str] = Header(None)):
    return f"User entered <i>{hx_prompt}</i>"