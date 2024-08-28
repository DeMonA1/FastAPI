from typing import List, Optional

from pydantic import BaseModel, EmailStr
from fastapi import Form

from models.events import Event


class User(BaseModel):
    email: EmailStr
    username: str
    events: Optional[List[Event]] = None
    
    @classmethod
    def as_form(cls, 
                email: EmailStr = Form(...),
                username: str = Form(...),
                password: str = Form(...)):
        return cls(email=email, username=username, password=password)
    
    
    class Config:
        json_schema_extra = {"example":{"email": "fastapi@example.com",
                                        "username": "strong",
                                        "events": [],}}
        

class UserSignIn(BaseModel):
    email: EmailStr
    password: str
    
    @classmethod
    def as_form(cls,
                email: EmailStr = Form(...),
                password: str = Form(...)):
        return cls(email=email, password=password)
    
    
class NewUser(User):
    password: str
    
    
    class Config:
        json_schema_extra = {"example": {"email": "fastapi@example.com",
                                         "password": "strongpassword",
                                         "username": "MYaPP"}}    