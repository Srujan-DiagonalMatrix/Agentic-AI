from __future__ import annotations

from fastapi import FastAPI
from app.config import settings
from app.db.session import engine, sessionLocal
from sqlalchemy import text

app = FastAPI(title=settings.app_name)

@app.get("/")
def root() -> dict:
    return{
        "message":f"Welcome to {settings.app_name}",        
        "environment":settings.app_env
    }

@app.post("/health")
def health() -> dict:

    db_status = "unknown"

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            db_status = "OK"

    except Exception as exc:
        db_status = f"error {str(exc)}"     

    return {
        "Status":"OK",
        "app_name": settings.app_name,
        "environment": settings.app_env,
        "database": db_status
    }