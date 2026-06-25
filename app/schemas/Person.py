from pydantic import BaseModel

class PersonCreate(BaseModel):
    LastName:str
    FirstName:str
    MiddleName:str
    SecretStuff:str

class PersonResponse(BaseModel):
    id: int
    LastName: str
    FirstName: str
    MiddleName: str

    class Config:
        from_attributes = True


class PersonResponseForEdit(BaseModel):
    id: int
    LastName:str
    FirstName:str
    MiddleName:str
    SecretStuff:str

    class Config:
        from_attributes = True


