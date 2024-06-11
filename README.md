# HTMX Examples utilizing FastAPI

This is an implementation of HTMX inside of FastAPI.  
I got the inspiration from <https://github.com/Konfuzian/htmx-examples-with-flask>.

Each example is written as a separate route in `backend/api/routes`

## Setup

```shell
pip install -r requirements.txt
```

## Run
### Python
```shell
cd backend
python ./main.py
```
### Uvicorn
```shell
cd backend
uvicorn main:app --reload --port 8000
```

The server will run on <http://localhost:8000>