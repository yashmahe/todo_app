from model import Todo, UserBase, Group
from pymongo import MongoClient
import ssl
import socket
import redis
import ast
import json


r = redis.Redis(host='localhost',port=6379)

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
    for document in cursor:
        todos.append(Todo(**document))
    return todos

def create_todo(todo):
    document = todo
    todo_id = document["id"]
    grp_title = document["group_title"]
    result =  collection.insert_one(document)
    todo_list = "todo_list_" + document["group_title"]
    grp_list = "group_list_" + document["group_title"]
    del document['_id']
    r.set(todo_list,json.dumps(document))
    is_group_present = False if (group.find_one({"title": grp_title}) == None) else True
    if is_group_present:
        new_group = r.get(grp_list)
        new_group = json.loads(new_group)
        #new_group = group.find_one({"title": document["group_title"]})
        new_group['id'].append(document['id'])
        new_group['task'].append(document['task'])
        new_group['due_date'].append(document['due_date'])
        new_group['is_completed'].append(document['is_completed'])
        new_group['assigned_to'].append(document['assigned_to'])
        r.set(grp_list,json.dumps(new_group))
        print(r.get(grp_list))
        group.update_one({"title": document["group_title"]}, {"$set": {"id":new_group['id'], "task": new_group['task'], "due_date": new_group['due_date'], "is_completed": new_group['is_completed'], "assigned_to":new_group['assigned_to']}})
    else:
        new_group = dict()
        new_group["title"] = document["group_title"]
        new_group['id'] = []
        new_group['id'].append(document['id'])
        new_group["task"] = []
        new_group['task'].append(document['task'])
        new_group["due_date"] = []
        new_group['due_date'].append(document['due_date'])
        new_group["is_completed"] = []
        new_group['is_completed'].append(document['is_completed'])
        new_group["assigned_to"] = []
        new_group['assigned_to'].append(document['assigned_to'])
        print(new_group)
        r.set(grp_list,json.dumps(new_group))
        group.insert_one(new_group)
    if document:
        return document

async def remove_group(title):
    grp_list = "group_list_" + title
    grp = r.get(grp_list)
    grp = grp.decode('utf-8')
    grp = json.loads(grp)
    is_all_task_completed = True
    for i in range(len(grp['is_completed'])):
        if grp['is_completed'][i] == False:
            is_all_task_completed = False 
            break
    if is_all_task_completed:
        group.delete_one({"title":title})
    return True

async def update_todo(id, task, due_date, is_completed, assigned_to):
    collection.update_one({"id": id}, {"$set": {"task": task, "due_date": due_date, "is_completed":is_completed, "assigned_to":assigned_to}})
    document =  collection.find_one({"id": id})
    del document['_id']
    todo_list = "todo_list_" + document["group_title"]
    r.set(todo_list, json.dumps(document)) 
    grp_list = "group_list_" + document["group_title"]
    grp = r.get(grp_list)
    grp = grp.decode('utf-8')
    grp = json.loads(grp) 
    idx = grp['id'].index(id)
    for i in grp:
        if i=='title':
            continue
        grp[i][idx] = document[i]
    r.set(grp_list, json.dumps(grp))
    group.delete_one({'title':document["group_title"]})
    group.insert_one(grp)

    return document

async def remove_todo(id):
    document = collection.find_one({"id": id})
    todo_list = "todo_list_" + document["group_title"]
    grp_list = "group_list_" + document["group_title"]
    document = r.get(todo_list)
    document = document.decode('utf-8')
    document = json.loads(document)
    grp = r.get(grp_list)
    grp = grp.decode('utf-8')
    grp = json.loads(grp) 
    idx = grp['id'].index(id)
    for i in grp:
        if i=='title':
            continue
        grp[i].pop(idx)
    #remove_group(document["group_title"])
    r.set(grp_list, json.dumps(grp))
    collection.delete_one({"id": id})
    group.delete_one({'title':document["group_title"]})
    group.insert_one(grp)
    return True
    
async def fetch_all_groups():
    todos = []
    cursor = group.find({})
    for document in cursor:
        todos.append(Group(**document))
    return todos