from fastapi import FastAPI

from app import database
from .routers import cabinets

database.init_db()
app = FastAPI(title="Personal Cabinet", version="0.0.1")

app.include_router(cabinets.router)

@app.get("/")
async def root():
    return {"message": "Alive and kicking!"}