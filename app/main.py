from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from app.database.init_db import create_tables
from fastapi.middleware.cors import CORSMiddleware

from app.routers.v1.problem import problemRouter
from app.routers.v1.source_code import sourceCodeRouter
from app.routers.v1.prediction import predictionRouter

@asynccontextmanager
async def lifespan(app : FastAPI):
    print('Created')
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://cse-lbds.site"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(problemRouter, prefix='/api/v1/problems')
app.include_router(sourceCodeRouter, prefix='/api/v1/source-code')
app.include_router(predictionRouter, prefix='/api/v1/prediction')

@app.get('/')
def home():
    return RedirectResponse(url='/docs')

# uvicorn app.main:app --host 0.0.0.0 --port 8000