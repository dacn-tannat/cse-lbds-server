from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from app.database.init_db import create_tables
from app.routers.v1.problem import problemRouter
from app.routers.v1.source_code import sourceCodeRouter

@asynccontextmanager
async def lifespan(app : FastAPI):
    print('Created')
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(problemRouter, prefix='/v1/problem')
app.include_router(sourceCodeRouter, prefix='/v1/source_code')

@app.get('/')
def home():
    return RedirectResponse(url='/docs')