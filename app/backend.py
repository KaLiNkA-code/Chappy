from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()


app.mount("/mainpage", StaticFiles(directory="frontend/mainpage"), name="mainpage")


templates = Jinja2Templates(directory="frontend/mainpage")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "main.html", {"request": request})


# @app.post("/nicepage.css")
# async def nacepage_func(request: Request):
#     return {}
