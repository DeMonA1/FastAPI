from pydantic import BaseModel, ConfigDict
from fastapi import Form
from typing import List, Optional


class Todo(BaseModel):
    id: Optional[int] = None
    item: str
    model_config = ConfigDict(json_schema_extra = {"example": {"id": 1,
                                        "item": "Example schema!"}})
    
    @classmethod
    def as_form(cls, item: str = Form(...)): 
        return cls(item=item)
        
        
class TodoItem(BaseModel):
    item: str
    model_config = ConfigDict(json_schema_extra = {"example": {"item": "Read the next chapter of the book"}})
        

class TodoItems(BaseModel):
    todos: List[TodoItem]
    model_config = ConfigDict(json_schema_extra = {"example": {"todos": [ {"item": "Example schema 1!"},
                                                    {"item": "Example schema 2!"}]}})
