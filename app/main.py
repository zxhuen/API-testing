from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.database import engine, Base
from app.api.Person import router as Person_Router
from app.api.Dog import router as Dog_Router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Person Test", lifespan=lifespan)

app.include_router(Person_Router)
app.include_router(Dog_Router)