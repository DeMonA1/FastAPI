from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr, ConfigDict

from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]] = None
    model_config = ConfigDict(json_schema_extra = {"example":{"email": "fastapi@example.com",
                                    "password": "strongpassword",
                                    "events": [],}})   
    
    
    class Settings:
        name = "users"
        

        

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    