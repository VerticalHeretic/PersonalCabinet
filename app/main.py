from fastapi import FastAPI
from app import database
from app.routers import items, cabinets

database.init_db()
app = FastAPI(title="Personal Cabinet", version="0.0.1")

app.include_router(cabinets.router)
app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Alive and kicking!"}