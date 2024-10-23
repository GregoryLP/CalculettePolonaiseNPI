from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes.calculation import router as calculations_router
from app.database import init_db

@asynccontextmanager
async def start(app: FastAPI):
    init_db()

app = FastAPI(start=start)

app.include_router(calculations_router, prefix="/calculations")

@app.get("/")
async def root():
    return {"message": "NPI Calculator API"}