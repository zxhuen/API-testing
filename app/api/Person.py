from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session  
from app.core.database import get_db
from app.schemas.Person import PersonResponse, PersonCreate
from app.services.person_services import add_Person, list_Person


router = APIRouter(prefix="/Person", tags=["Person"])

@router.post("/", response_model=PersonResponse)
def create(Person: PersonCreate, db: Session = Depends(get_db)):
    return add_Person(db, Person)


@router.get("/", response_model=PersonResponse)
def get_all(db: Session = Depends(get_db)):
    return list_Person(db)

