from sqlalchemy.orm import session
from app.repository.Dog_Repo import create_Dog, get_Dog
from app.schemas.Dog import DogCreate

def add_dog(db: session, Dog: DogCreate):
    return create_Dog(db, Dog)

def list_Dog(db: session):
    return get_Dog(db)


