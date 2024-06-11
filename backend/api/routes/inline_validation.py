import random, string
from typing import List, Optional, Annotated
from fastapi import APIRouter, Depends, Body, Form
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

def validate_email(email):
    return email == "test@test.com"

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("inline_validation/index.html", context)

@router.post("/contact", response_class=HTMLResponse)
def contact(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("inline_validation/index.html", context)

@router.post("/contact/email", response_class=HTMLResponse)
def contact_edit(request: Request, email: Annotated[str, Form()]):
    context = {'request': request}
    if not validate_email(email):
        return templates.TemplateResponse("inline_validation/partial_error.html", context)
    return templates.TemplateResponse("inline_validation/partial_valid.html", context)