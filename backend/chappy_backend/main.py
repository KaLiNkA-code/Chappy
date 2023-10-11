from fastapi import FastAPI, Request
import uvicorn
from enum import Enum


class ModelName(str, Enum):
    chat_id = 'alexnet'
    photo = 'resnet'
    text = 'lenet'
    post_data = 'lenet'


app = FastAPI()


@app.get("/")
async def root(request: Request):
    return {"status": "ok", "message": "Hello World from backend"}


@app.get("/users/{user_chat_id}/posting")
async def get_model(user_chat_id: int):
    return {"user_chat_id": user_chat_id, "message": "Have some residuals"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5051, reload=True, workers=3)
