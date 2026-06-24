from sqlalchemy.orm import Session
from app.models.Dog import Dog
from app.schemas.Dog import DogCreate

def create_Dog(db: Session, Dogs: DogCreate):
    db_Dog = Dog(**Dogs.model_dump())

    db.add(db_Dog)
    db.commit()
    db.refresh(db_Dog)

    return db_Dog

def get_Dog(db: Session):
    return db.query(Dog).all()

def get_dog_id(db: Session, ID: int):
    return db.query(Dog).filter(Dog.id == ID).first()