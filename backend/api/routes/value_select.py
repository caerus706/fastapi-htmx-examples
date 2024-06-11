import random, string
from typing import List, Optional, Annotated
from fastapi import APIRouter, Depends, Body, Form
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

data = {
    "audi": {"models": ["A1", "A4", "A6"]},
    "toyota": {"models": ["Landcruiser", "Tacoma", "Yaris"]},
    "bmw": {"models": ["325i", "325ix", "X5"]},
}


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    current_make = "audi"
    context = {'request': request, "makes": data.keys(), "current_make": current_make, "models":data[current_make]["models"]}
    return templates.TemplateResponse("value_select/index.html", context)

@router.get("/models", response_class=HTMLResponse)
def index(request: Request, make: str):
    context = {'request': request, "makes": data.keys(), "current_make": make, "models":data[make]["models"]}
    return templates.TemplateResponse("value_select/partial_models.html", context)