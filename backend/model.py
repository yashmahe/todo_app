from pydantic import BaseModel

class Todo(BaseModel):
    id: str 
    task: str
    due_date: str
    is_completed: bool
    assigned_to: str
    group_title: str

class UserBase(BaseModel):
    username: str 
    email: str 
    password: str 

class Group(BaseModel):
    title: str 
    id: list 
    task: list 
    due_date: list 
    is_completed: list 
    assigned_to: list 


class UserDisplay(BaseModel):
    username: str 
    email: str 


    

