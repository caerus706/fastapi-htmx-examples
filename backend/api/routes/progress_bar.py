from time import sleep
from math import floor
from random import random
from typing import List, Optional, Annotated
from fastapi import APIRouter, Depends, Body, Form
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

percentage = 0

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("progress_bar/index.html", context)

@router.post("/start", response_class=HTMLResponse)
def start(request: Request):
    global percentage
    percentage = 0
    context = {'request': request, "percentage": percentage, "complete": False}
    return templates.TemplateResponse("progress_bar/in_progress.html", context)

@router.get("/job", response_class=HTMLResponse)
def job(request: Request):
    context = {'request': request, "percentage": percentage, "complete": percentage >= 100}
    return templates.TemplateResponse("progress_bar/in_progress.html", context)

@router.get("/job/progress", response_class=HTMLResponse)
def progress(request: Request):
    global percentage
    percentage += floor(33 * random())
    context = {'request': request, "percentage": percentage, "complete": percentage >= 100}
    hx_header = {"HX-Trigger": "done"}
    return templates.TemplateResponse("progress_bar/in_progress.html", context, headers=hx_header)