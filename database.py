
from model import Todo, UserBase
from pymongo import MongoClient
import ssl
import socket

cluster = MongoClient("mongodb+srv://yashm:yashmahe@cluster0.c5wwa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
db = cluster["TodoList"]
user = db["userlist"]
group = db["group"]
collection = db["todo"]

async def create_user(UserBase):
    document = UserBase
    result =  user.insert_one(document)
    return document



async def fetch_one_todo(id):
    document =  collection.find_one({"id": id})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    grp_title = document["group_title"]
    result =  collection.insert_one(document)
    is_group_present = False if (group.find_one({"title": grp_title}) == None) else True

    if is_group_present:
        task_list = group.find_one({"title": document["group_title"]})
        task_list["tasks"].append(document)
        group.update_one({"title": document["group_title"]}, {"$set": {"tasks": task_list}})
    else:
        new_group = dict()
        new_group["title"] = document["group_title"]
        new_group["tasks"] = []
        new_group["tasks"].append(document)
        group.insert_one(new_group)
    if document:
        return document

async def remove_group(title):
    task_list = group.find_one({"title":title})
    task_list = task_list["tasks"]["tasks"]
    print(task_list)
    is_all_task_completed = True
    for i in range(len(task_list)):
        if task_list[i]["is_completed"] == False:
            is_all_task_completed = False 
            break
        #print(task_list[i]["is_completed"])
    if is_all_task_completed:
        group.delete_one({"title":title})
    return task_list

async def update_todo(id, task, due_date, is_completed, assigned_to):
    collection.update_one({"id": id}, {"$set": {"task": task, "due_date": due_date, "is_completed":is_completed, "assigned_to":assigned_to}})
    document =  collection.find_one({"id": id})
    return document

async def remove_todo(id):
    collection.delete_one({"id": id})
    return True