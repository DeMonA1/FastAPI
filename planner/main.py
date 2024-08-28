from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes.users import user_router
from routes.events import event_router

import uvicorn


app = FastAPI()

# Register routes

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)