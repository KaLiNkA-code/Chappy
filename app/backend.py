from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    response =  templates.TemplateResponse(
        "main.html", {"request": request})
    print(type(response))
    return response


# @app.post("/nicepage.css")
# async def nacepage_func(request: Request):
#     return {}
