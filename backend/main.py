import uvicorn
from typing import Optional
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from api.api import api_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse, tags=['Index'])
def index(request: Request, hx_request: Optional[str] = Header(None)): #hx-request
    
    context = {'request': request}
    return templates.TemplateResponse("index.html", context)

# simple test
@api_router.get('/ping', tags=['test'])
def ping():
    return "pong"

app.include_router(api_router) #, prefix="/")
# def config():
#     print("ran config")

# config()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info", reload=True)