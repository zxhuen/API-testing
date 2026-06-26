from sqlalchemy.orm import session
from app.repository.Dog_Repo import create_Dog, get_Dog, get_dog_id, delete_dog_repo, get_dog_filter
from app.schemas.Dog import DogCreate

def add_dog(db: session, Dog: DogCreate):
    return create_Dog(db, Dog)

def list_Dog(db: session):
    return get_Dog(db)

def get_Dog_ID(db: session, ID: int):
    return get_dog_id(db, ID)

def delete_dog_service(db: session, ID: int):
    return delete_dog_repo(db, ID)

def select_dog_filter_services(db: session, skip: int, limit: int):
    return get_dog_filter(db, skip, limit)




