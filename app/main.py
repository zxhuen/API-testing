from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.database import engine, Base
from app.api.Person import router as Person_Router
from app.api.Dog import router as Dog_Router




app = FastAPI(title="Person Test")

app.include_router(Person_Router)
app.include_router(Dog_Router)