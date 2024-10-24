from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.calculation import router as calculations_router
from database import init_db

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await init_db()

app.include_router(calculations_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "NPI Calculator API"}