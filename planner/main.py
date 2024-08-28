from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.connection import conn
from contextlib import asynccontextmanager

from routes.users import user_router
from routes.events import event_router

import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    conn()
    yield

app = FastAPI(lifespan=lifespan)

# Register routes

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)