from fastapi import FastAPI
from .api import endpoints, favorites

app = FastAPI(title="What Can I Cook? API")

app.include_router(endpoints.router, prefix="/api", tags=["recipes"])
app.include_router(favorites.router, prefix="/api", tags=["favorites"])

@app.get("/")
async def root():
    return {"message": "Welcome to What Can I Cook? API"}
