from fastapi import FastAPI

app = FastAPI(title="Personal Cabinet", version="0.0.1")

@app.get("/")
async def root():
    return {"message": "Alive and kicking!"}