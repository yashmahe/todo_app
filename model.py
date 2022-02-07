from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    text: str 
    due_date: str 
    is_completed: str 
    assigned_to: str 
    
