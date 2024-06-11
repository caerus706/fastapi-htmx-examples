import random, string
from time import sleep
from typing import List, Optional, Annotated
from fastapi import APIRouter, Depends, Body, Form
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

color_options = ["red", "blue", "green", "orange"]
color_index = 0

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("animations/index.html", context)

@router.get("/colors", response_class=HTMLResponse)
async def colors(request: Request):
    global color_index
    color_index = (color_index + 1) % len(color_options)
    context = {'request': request, "color": color_options[color_index]}
    return templates.TemplateResponse("animations/color_swap.html", context)

@router.delete("/fade_out_demo")
def fade_out(request: Request):
    return ""

@router.post("/fade_in_demo")
def fade_in(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("animations/fade_in_on_addition.html", context)

@router.post("/name")
def name(request: Request):
    sleep(0.5)
    return "Submitted!"

@router.get("/initial-content")
def initial_content(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("animations/view_transition_initial.html", context)

@router.get("/new-content")
def new_content(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("animations/view_transition_new.html", context)