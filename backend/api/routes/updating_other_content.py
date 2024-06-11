from typing import Annotated
from fastapi import APIRouter, Form
from fastapi import Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

data = [
    {
        "name": "Joe Smith",
        "email": "joe@smith.org",
    },
    {
        "name": "Angie MacDowell",
        "email": "angie@macdowell.org",
    },
]

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request, "contacts": data}
    return templates.TemplateResponse("updating_other_content/index.html", context)


@router.post("/contacts1", response_class=HTMLResponse)
def contacts1(request: Request, name: Annotated[str, Form()], email: Annotated[str, Form()]):
    data.append({
        "name": name,
        "email": email
    })
    context = {'request': request, "contacts": data}
    return templates.TemplateResponse("updating_other_content/partial_1.html", context)


@router.post("/contacts2", response_class=HTMLResponse)
def contacts2(request: Request, name: Annotated[str, Form()], email: Annotated[str, Form()]):
    contact = {
        "name": name,
        "email": email
    }
    
    data.append(contact)
    context = {'request': request, "contact": contact}
    return templates.TemplateResponse("updating_other_content/partial_2.html", context)


@router.post("/contacts3")
def contacts3(name: Annotated[str, Form()], email: Annotated[str, Form()]):
    data.append({
        "name": name,
        "email": email
    })
    return Response(content="", headers={"HX-Trigger": "newContact"})
    # context = {'request': request, "contacts": data}
    # return templates.TemplateResponse("updating_other_content/partial_3.html", context)

@router.get("/contacts3/table", response_class=HTMLResponse)
def contacts3_table(request: Request):
    context = {'request': request, "contacts": data}
    return templates.TemplateResponse("updating_other_content/partial_table.html", context)


@router.post("/contacts4", response_class=HTMLResponse)
def contacts4(request: Request, name: Annotated[str, Form()], email: Annotated[str, Form()]):
    data.append({
        "name": name,
        "email": email
    })
    context = {'request': request, "contacts": data}
    return templates.TemplateResponse("updating_other_content/partial_4.html", context)


@router.get("/contacts4/table", response_class=HTMLResponse)
def contacts4_table(request: Request):
    context = {'request': request, "contacts": data}
    return templates.TemplateResponse("updating_other_content/partial_table.html", context)
