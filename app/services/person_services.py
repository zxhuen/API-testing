from sqlalchemy.orm import Session
from app.repository.Person_Repo import create_person, get_person, get_person_ID
from app.schemas.Person import PersonCreate

def add_Person(db: Session, person: PersonCreate):
    return create_person(db, person)

def list_Person(db: Session):
    return get_person(db)

def get_person_id(db: Session, personID: int):
    return get_person_ID(db, personID)
