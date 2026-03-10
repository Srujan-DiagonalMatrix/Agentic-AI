from __future__ import annotations

from fastapi import FastAPI
from app.config import settings

app = FastAPI(title=settings.app_name)

@app.get("/")
def root() -> dict:
    return{
        "message":f"Welcome to {settings.app_name}",        
        "environment":settings.app_env
    }

@app.post("/health")
def health() -> dict:
    return {
        "Status":"OK",
        "app_name": settings.app_name,
        "environment": settings.app_env
    }