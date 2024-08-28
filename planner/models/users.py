from pydantic import BaseModel, EmailStr
from typing import List, Optional
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]] = None
    
    class Config:
        json_schema_extra = {"example":{"email": "fastapi@example.com",
                                        "password": "strongpassword",
                                        "events": [],}}
        

class UserSignIn(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        json_schema_extra = {"example":{"email": "fastapi@example.com",
                                        "password": "strongpassword",}}