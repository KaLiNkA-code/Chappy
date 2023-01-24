from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse


app = FastAPI()


@app.get("/")
async def root():
    return FileResponse("mainpage/index.html")
