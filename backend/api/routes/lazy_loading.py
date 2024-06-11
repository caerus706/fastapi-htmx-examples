import random, string
from typing import List, Optional, Annotated
from fastapi import APIRouter, Depends, Body, Form
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("lazy_loading/index.html", context)

@router.get("/graph", response_class=HTMLResponse)
def graph(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("lazy_loading/image.html", context)