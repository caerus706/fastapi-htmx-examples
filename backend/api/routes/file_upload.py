from fastapi import APIRouter, UploadFile
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("file_upload/index.html", context)

@router.post("/upload")
def upload_hyperscript(file: UploadFile):
    return {"filename": file.filename}