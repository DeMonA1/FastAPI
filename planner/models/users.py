from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]
    
    class Settings:
        name = "users"
        
        
    class Config:
        json_schema_extra = {"example":{"email": "fastapi@example.com",
                                        "password": "strongpassword",
                                        "events": [],}}
        

class UserSignIn(BaseModel):
    email: EmailStr
    password: str
    