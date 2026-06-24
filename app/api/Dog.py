from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session  
from app.core.database import get_db
from app.schemas.Dog import DogResponse, DogCreate
from app.services.dog_services import add_dog, list_Dog

router = APIRouter(prefix = "/Dog", tags=["Dog"])

@router.post("/", response_model=DogResponse)
def crete_Dog(Dog: DogCreate, db: Session = Depends(get_db)):
    return add_dog(db, Dog)

@router.get("/", response_model=list[DogResponse])
def get_all(db: Session = Depends(get_db)):
    return list_Dog(db)