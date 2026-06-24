from sqlalchemy import Column, Integer, String, DateTime, func
from app.core.database import Base

class Person(Base):
    __tablename__ = "Person"

    id = Column(Integer, primary_key=True, index=True)
    LastName = Column(String, nullable=False)
    FirstName = Column(String, nullable=False)
    MiddleName = Column(String, nullable=True)
    SecretStuff = Column(String, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

