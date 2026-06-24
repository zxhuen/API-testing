from sqlalchemy import Column, Integer, String, DateTime, func
from app.core.database import Base

class Dog(Base):
    __tablename__ = "Dog"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    secretStuff = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())