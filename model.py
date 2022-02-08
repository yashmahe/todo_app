from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int 
    task: str
    due_date: str
    is_completed: bool 
    assigned_to: str
    group_title: str

class UserBase(BaseModel):
    username: str 
    email: str 
    password: str 

class UserDisplay(BaseModel):
    username: str 
    email: str 

# class groupedTask(BaseModel):
#     title: str
#     task: list()=[] 



    

