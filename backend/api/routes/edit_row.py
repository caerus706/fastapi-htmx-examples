import random, string
from typing import List, Optional, Annotated
from fastapi import APIRouter, Depends, Body, Form
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

data = [
    {
        "id": 0,
        "name": "Joe Smith",
        "email": "joe@smith.org",
    },
    {
        "id": 1,
        "name": "Angie MacDowell",
        "email": "angie@macdowell.org",
    },
    {
        "id": 2,
        "name": "Fuqua Tarkenton",
        "email": "fuqua@tarkenton.org",
    },
    {
        "id": 3,
        "name": "Kim Yee",
        "email": "kim@yee.org",
    },
]


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request, 'contacts': data }
    return templates.TemplateResponse("edit_row/index.html", context)


@router.get("/contact/{id}", response_class=HTMLResponse)
def get_contact(request: Request, id: int):
    context = {'request': request, 'contact': data[id] }
    return templates.TemplateResponse("edit_row/partial.html", context)


@router.put("/contact/{id}", response_class=HTMLResponse)
def put_contact(request: Request, id: int, name: str = Form(), email: str = Form()):
    data[id] = {'name': name, 'email': email}
    context = {'request': request, 'contact': data[id] }
    return templates.TemplateResponse("edit_row/partial.html", context)

@router.get("/contact/{id}/edit", response_class=HTMLResponse)
def contact_edit(request: Request, id: int):
    context = {'request': request, 'contact': data[id] }
    return templates.TemplateResponse("edit_row/edit.html", context)