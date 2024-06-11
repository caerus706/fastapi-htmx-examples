import random, string
from typing import List, Optional, Annotated
from fastapi import APIRouter, Depends, Body, Form
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

def generate_contacts(page=1, page_size=10):
    def generate_contact(i):
        def generate_id(n=10):
            return "".join(random.choices(string.ascii_uppercase + string.digits, k=n))

        return {"name": "Agent Smith", "email": f"void{page * page_size + i}@null.org", "id": generate_id()}

    return [generate_contact(i) for i in range(page_size)]

@router.get("/", response_class=HTMLResponse)
def index(request: Request, page: int = 1):
    context = {'request': request, 'contacts': generate_contacts(page=page), 'page': page }
    return templates.TemplateResponse("click_to_load/index.html", context)

@router.get("/contacts", response_class=HTMLResponse)
def contacts(request: Request, page: int = 1):
    context = {'request': request, 'contacts': generate_contacts(page=page), 'page': page }
    return templates.TemplateResponse("click_to_load/partial.html", context)

