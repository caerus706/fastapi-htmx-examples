import random, string
from typing import List, Optional, Annotated
from fastapi import APIRouter, Depends, Body, Form
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

data = {
    0: {
        "name": "Joe Smith",
        "email": "joe@smith.org",
        "status": "Active",
    },
    1: {
        "name": "Angie MacDowell",
        "email": "angie@macdowell.org",
        "status": "Active",
    },
    2: {
        "name": "Fuqua Tarkenton",
        "email": "fuqua@tarkenton.org",
        "status": "Active",
    },
    3: {
        "name": "Kim Yee",
        "email": "kim@yee.org",
        "status": "Inactive",
    },
}

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request, 'contacts': data }
    return templates.TemplateResponse("delete_row/index.html", context)

@router.delete("/contact/{id}", response_class=HTMLResponse)
def delete_contact(request: Request, id: int):
    del data[id]
    context = {'request': request, 'contacts': data }
    return templates.TemplateResponse("delete_row/index.html", context)
