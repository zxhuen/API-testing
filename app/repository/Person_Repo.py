from sqlalchemy.orm import Session
from app.models.Person import Person
from app.schemas.Person import PersonCreate

def create_person(db: Session, Persons: PersonCreate):
    db_person = Person(**Persons.model_dump())

    db.add(db_person)
    db.commit()
    db.refresh(db_person)

    return db_person

def get_person(db: Session):
    return db.query(Person).all()

def get_person_ID(db: Session, person_id: int):
    return db.query(Person).filter(Person.id == person_id).first()