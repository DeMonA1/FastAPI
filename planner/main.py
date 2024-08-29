from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from routes.users import user_router
from routes.events import event_router
from database.connection import Settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await settings.initialize_database()
    yield

app = FastAPI(lifespan=lifespan)

settings = Settings()

origins = ["*"]

# Register routes

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")
app.add_middleware(CORSMiddleware,
                   allow_origins=origins, allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])

@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)