from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: int
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
    

    