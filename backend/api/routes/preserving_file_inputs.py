from typing import Annotated
from fastapi import APIRouter, UploadFile, File
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("preserving_file_inputs/index.html", context)

@router.post("/upload")
def upload_hyper(file: UploadFile = None):
    # return {"filename": file.filename}
    return "Uploaded!"
# def upload_hyper(file: Annotated[bytes, File()]):