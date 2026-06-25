from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session  
from app.core.database import get_db
from app.schemas.Dog import DogResponse, DogCreate
from app.services.dog_services import add_dog, list_Dog, get_Dog_ID, delete_dog_service

router = APIRouter(prefix = "/Dog", tags=["Dog"])

@router.post("/", response_model=DogResponse)
def crete_Dog(Dog: DogCreate, db: Session = Depends(get_db)):
    return add_dog(db, Dog)

@router.get("/", response_model=list[DogResponse])
def get_all(db: Session = Depends(get_db)):
    return list_Dog(db)

@router.get("/{Dog_ID}", response_model=DogResponse)
def get_dog_ID(Dog_ID: int, db: Session = Depends(get_db)):
    dog = get_Dog_ID(db, Dog_ID)

    if not dog:
        raise HTTPException(
            status_code=404,
            detail="No dog found"
        )
    
    return dog

@router.delete("/{Dog}")
def delete_dog_ID(ID: int, db: Session = Depends(get_db)):
    dog = delete_dog_service(db, ID)

    if not dog:
        raise HTTPException(
            status_code=404,
            detail= "no dog found"
        )
    
    return dog
        