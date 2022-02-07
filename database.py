
from model import Todo
from pymongo import MongoClient
import ssl
import socket


cluster = MongoClient("mongodb+srv://yashm:yashmahe@cluster0.c5wwa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
db = cluster["Todo_List"]
collection = db["todo"]

async def fetch_one_todo(id):
    document = collection.find_one({"id": id})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = collection.insert_one(document)
    return document


async def update_todo(id, desc):
    collection.update_one({"id": id}, {"$set": {"description": desc}})
    document = collection.find_one({"id": id})
    return document

async def remove_todo(id):
    collection.delete_one({"id": id})
    return True