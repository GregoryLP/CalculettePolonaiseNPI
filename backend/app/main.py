"""Main module of the API that contains the FastAPI application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.calculation import router as calculations_router
from app.database import init_db

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    """Initialize the database connection"""
    await init_db()

app.include_router(calculations_router, prefix="/api")

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "NPI Calculator API"}
