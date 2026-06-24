from pydantic import BaseModel

class DogCreate(BaseModel):
    name: str
    age: int
    secretStuff: str


class DogResponse(BaseModel):
    id: int
    name: str
    age: int

    class config:
        form_attributes=True
