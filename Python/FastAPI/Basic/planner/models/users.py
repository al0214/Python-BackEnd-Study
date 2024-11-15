from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    # events: Optional[List[Event]]

    class Settings:
        name = "users"

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapit@packt.com",
                "username": "string!!!",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapit@packt.com",
                "username": "string!!!",
                "events": [],
            }
        }
