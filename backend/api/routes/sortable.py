from typing import List, Optional
from fastapi import APIRouter, Header, Form, Query
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder

router = APIRouter()

templates = Jinja2Templates(directory="templates")

global dataArray
dataArray = [
    {'item': 1},
    {'item': 2},
    {'item': 3},
    {'item': 4},
    {'item': 5}
]

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    global dataArray
    context = {'request': request, 'data': dataArray}
    return templates.TemplateResponse("sortable/index.html", context)

@router.post("/items")
async def items(request: Request, item: List[int] = Form(None)):
    global dataArray

    # seems to fire twice at times
    if (item is not None):
        newArray = []
        for i in item:
            newArray.append({'item': i})
        dataArray = newArray

    context = {'request': request, 'data': dataArray}
    return templates.TemplateResponse("sortable/index.html", context)