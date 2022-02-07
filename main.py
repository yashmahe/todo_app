from fastapi import FastAPI, HTTPException

from model import Todo

from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000",
]

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
    response = fetch_all_todos()
    return response

@app.get("/api/todo/{id}", response_model=Todo)
async def get_todo_by_id(id):
    response = fetch_one_todo(id)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the id {id}")

@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo):
    document = todo.dict()
    response = create_todo(document)
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/todo/{id}/", response_model=Todo)
async def put_todo(id: int, text: str,due_date: str, is_completed: str, assigned_to: str):
    response = update_todo(id, text,due_date, is_completed, assigned_to)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the id {id}")

@app.delete("/api/todo/{id}")
async def delete_todo(id):
    response = remove_todo(id)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the id {id}")