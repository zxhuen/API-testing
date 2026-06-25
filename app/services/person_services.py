from sqlalchemy.orm import Session
from app.repository.Person_Repo import create_person, get_person, get_person_ID, delete_person_repo, edit_person_repo
from app.schemas.Person import PersonCreate, PersonResponseForEdit

def add_Person(db: Session, person: PersonCreate):
    return create_person(db, person)

def list_Person(db: Session):
    return get_person(db)

def get_person_id(db: Session, personID: int):
    return get_person_ID(db, personID)

def delete_person_services(db: Session, personID: int):
    return delete_person_repo(db, personID)

def edit_person_services(db: Session, personID: int, pc: PersonResponseForEdit):
    return edit_person_repo(db, personID, pc)
