from sqlalchemy.orm import Session
from app.models.Person import Person
from app.schemas.Person import PersonCreate, PersonResponseForEdit

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

def delete_person_repo(db: Session, person_id: int):
    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        return None

    db.delete(person)
    db.commit()

    return person


def edit_person_repo(db: Session, peron_id: int, personCreate: PersonResponseForEdit):
    person = db.query(Person).filter(Person.id == peron_id).first()

    if not person:
        return None
    
    person.LastName = personCreate.LastName
    person.FirstName = personCreate.FirstName
    person.MiddleName = personCreate.MiddleName
    person.SecretStuff = personCreate.SecretStuff

    db.commit()
    db.refresh(person)

    return person


def get_person_repo(db: Session, skip: int, limit: int):
    return (
        db.query(Person).offset(skip).limit(limit).all()
    )
    