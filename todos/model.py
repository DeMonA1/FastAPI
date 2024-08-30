from pydantic import BaseModel
from fastapi import Form
from typing import List, Optional


class Todo(BaseModel):
    id: Optional[int] = None
    item: str
    
    @classmethod
    def as_form(cls, item: str = Form(...)): 
        return cls(item=item)


    class ConfigDict:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Example schema!"
            }
        }
        
        
class TodoItem(BaseModel):
    item: str
    
    class ConfigDict:
        json_schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }
        

class TodoItems(BaseModel):
    todos: List[TodoItem]
    
    class ConfigDict:
        json_schema_extra = {"example": {"todos": [
                    {"item": "Example schema 1!"},
                    {"item": "Example schema 2!"}
                ]
            }
        }