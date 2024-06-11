from typing import List, Optional
from fastapi import APIRouter, Depends, Body, Form
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

router = APIRouter()

templates = Jinja2Templates(directory="templates")

class Contact(BaseModel):
    firstName: str
    lastName: str
    email: str

data = [
    {
        "firstName": "Joe",
        "lastName": "Blow",
        "email": "joe@blow.com",
    }
]

@router.get("/", response_class=HTMLResponse)
def click_edit_index(request: Request, id: int = 0):
    context = {'request': request, 'contact': data[id] }
    return templates.TemplateResponse("click_to_edit/index.html", context)

@router.get("/contact/{id}", response_class=HTMLResponse)
def get_contact(request: Request,id: int = 0):
    context = {'request': request, 'contact': data[id] }
    return templates.TemplateResponse("click_to_edit/index.html", context)

# @router.put("/contact/{id}")
# def put_contact(id: int, request: Request):
#     data[id] = {k: request.form[k] for k in ("firstName", "lastName", "email")}
#     context = {'request': request, 'contact': data[id] }
#     return templates.TemplateResponse("click_to_edit/index.html", context)

@router.put("/contact/{id}")
def put_form_contact(request: Request, id: int = 0, firstName: str = Form(), lastName: str = Form(), email: str = Form()):
    data[id] = {'firstName': firstName, 'lastName': lastName, 'email': email}
    context = {'request': request, 'contact': data[id] }
    return templates.TemplateResponse("click_to_edit/index.html", context)


@router.get("/contact/{id}/edit", response_class=HTMLResponse)
def contact_edit(request: Request, id: int = 0):
    context = {'request': request, 'contact': data[id] }
    return templates.TemplateResponse("click_to_edit/edit.html", context)