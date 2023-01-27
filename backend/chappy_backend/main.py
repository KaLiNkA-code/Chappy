from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root(request: Request):
    return {"status": "ok", "message": "Hello World from backend"}