from pydantic import BaseModel

class DogCreate(BaseModel):
    name: str
    owner_id: int | None
    age: int
    secretStuff: str


class DogResponse(BaseModel):
    id: int
    owner_id: int | None
    name: str
    age: int

    class config:
        form_attributes=True


