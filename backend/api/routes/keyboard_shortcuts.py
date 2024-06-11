from fastapi import APIRouter, UploadFile
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("keyboard_shortcuts/index.html", context)

@router.post("/doit")
def do_it():
    return "Did it!"