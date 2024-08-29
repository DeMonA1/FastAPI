from typing import List, Optional

from beanie import Document
from pydantic import BaseModel



class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
    
    
    class Config:
        json_schema_extra = {"example":{"title":"FastAPI Launch",
                                        "image": "https://unsplash.com/photos/blue-and-green-abstract-painting-Jd09hiCUPCs",
                                        "description": "We will be discussing the contents of the \
                                                        FastAPI in this event. Ensure to come with \
                                                        your own copy to win gifts!",
                                        "tags": ["python", "fastapi", "book", "launch"],
                                        "location": "Google Meet"}}
        
    class Settings:
        name = "events"
    
    
class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None
    
    
    class Config:
        json_schema_extra = {"example":{"title":"FastAPI Launch",
                                        "image": "https://unsplash.com/photos/blue-and-green-abstract-painting-Jd09hiCUPCs",
                                        "description": "We will be discussing the contents of the \
                                                        FastAPI in this event. Ensure to come with \
                                                        your own copy to win gifts!",
                                        "tags": ["python", "fastapi", "book", "launch"],
                                        "location": "Google Meet"}}

    