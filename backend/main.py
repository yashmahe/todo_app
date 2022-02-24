from fastapi import FastAPI, HTTPException

from model import Todo, UserBase

from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
    create_user,
    remove_group,
    fetch_all_groups
)

# an HTTP-specific exception class  to generate exception information

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000",
]

# what is a middleware? 
# software that acts as a bridge between an operating system or database and applications, especially on a network.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/group")
async def get_group():
    response = await fetch_all_groups()
    return response

@app.get("/api/todo/{id}", response_model=Todo)
async def get_todo_by_title(id):
    response = await fetch_one_todo(id)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the id {id}")

@app.post("/api/", response_model=UserBase) 
async def create__user(user: UserBase):
    response = await create_user(user.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.post("/api/todo/", response_model=Todo)
def post_todo(todo: Todo):
    response = create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/todo/{id}/", response_model=Todo)
async def put_todo(id: str, task: str, due_date: str, is_completed: str, assigned_to: str):
    response = await update_todo(id, task, due_date, is_completed, assigned_to)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the id {id}")

@app.delete("/api/todo/{id}")
async def delete_todo(id):
    response = await remove_todo(id)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the id {id}")

@app.delete("/api/group/{title}")
async def delete_group(title):
    response = await remove_group(title)
    if response:
        return "Successfully executed"
    raise HTTPException(404, f"There is no group with the title {title}")
