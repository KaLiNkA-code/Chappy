from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import httpx
import requests


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# @app.get("/")
# async def root(request: Request):
#     response =  templates.TemplateResponse(
#         "main.html", {"request": request})
#     print(type(response))
#     return response


@app.get("/api")
async def root_api(request: Request):
    response = requests.get("http://localhost:5051/")
    print(response)
    data = response.json()
    return {"status": "ok", "message": "Hello World from frontend", "data": data}

@app.get("/post/{user_chat_id}")
async def root_api(request: Request, user_chat_id: int):
    response = requests.get(f"http://localhost:5051/users/{user_chat_id}/posting")
    print(response)
    data = response.json()
    return {"status": "ok", "message": "Hello World from frontend", "data": data}


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=5050, reload=True, workers=3)
