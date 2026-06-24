from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session  
from app.core.database import get_db
from app.schemas.Person import PersonResponse, PersonCreate
from app.services.person_services import add_Person, list_Person, get_person_id, delete_person_services


router = APIRouter(prefix="/Person", tags=["Person"])

@router.post("/", response_model=PersonResponse)
def create(Person: PersonCreate, db: Session = Depends(get_db)):
    return add_Person(db, Person)


@router.get("/", response_model=list[PersonResponse])
def get_all(db: Session = Depends(get_db)):
    return list_Person(db)


@router.get("/{person_id}", response_model=PersonResponse)
def get_Person_ID(person_id: int, db: Session = Depends(get_db)):
    person = get_person_id(db, person_id)

    if not person:
        raise HTTPException(
            status_code=404,
            detail="Person not found"
        )
    
    return person

@router.delete("{Person_ID}")
def delete_person(ID: int, db: Session = Depends(get_db)):
    person = delete_person_services(db, ID)

    if not person:
        raise HTTPException(
            status_code=404,
            detail="no person found"
        )
    
    return {"message": "Person deleted successfully"}


