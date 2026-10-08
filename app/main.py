from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .database import Base, engine
from . import models
from .routes import chat

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Employee",
    version="1.0.0"
)

app.include_router(chat.router)

app.mount(
    "/",
    StaticFiles(directory="static", html=True),
    name="static"
)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "AI Employee"
    }
