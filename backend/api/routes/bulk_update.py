from typing import List, Optional, Annotated
from fastapi import APIRouter, Depends, Body, Form
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

router = APIRouter()

templates = Jinja2Templates(directory="templates")

data = [
    {
        "name": "Joe Smith",
        "email": "joe@smith.org",
        "status": "Active",
    },
    {
        "name": "Angie MacDowell",
        "email": "angie@macdowell.org",
        "status": "Active",
    },
    {
        "name": "Fuqua Tarkenton",
        "email": "fuqua@tarkenton.org",
        "status": "Active",
    },
    {
        "name": "Kim Yee",
        "email": "kim@yee.org",
        "status": "Inactive",
    },
]

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request, 'contacts': data }
    return templates.TemplateResponse("bulk_update/index.html", context)

@router.put("/activate", response_class=HTMLResponse)
def activate(request: Request, ids: Annotated[list, Form()]):
    print(ids)
    for id in ids:
        data[int(id)]["status"] = "Active"
    context = {'request': request, 'contacts': data }
    return templates.TemplateResponse("bulk_update/index.html", context)

@router.put("/deactivate", response_class=HTMLResponse)
def activate(request: Request, ids: Annotated[list, Form()]):
    for id in ids:
        data[int(id)]["status"] = "Inactive"
    context = {'request': request, 'contacts': data }
    return templates.TemplateResponse("bulk_update/index.html", context)