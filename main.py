from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class UserCreate(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50,
        description="Nom de l'utilisateur"
    )

    email: EmailStr = Field(
        description="Adresse email valide"
    )

    age: int = Field(
        ge=18,
        le=100
    )


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/users")
def create_user(user: UserCreate):
    return {"user": user}