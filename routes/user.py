from bson import ObjectId
from fastapi import APIRouter

from models.user import User,Student,Teacher
from config.db import conn
from schemas.user import userEntity,usersEntity

user= APIRouter()

@user.get('/users')
async def find_all_users():
    return usersEntity(conn.local.user.find())

@user.post('/')
async def create_user(user:User):
    conn.local.user.insert_one(dict(user))
    return usersEntity(conn.local.user.find())

@user.put('/{id}')
async def update_user(id,user:User):
    conn.local.user.find_one_and_update({'_id':ObjectId(id)},{'$set':dict(user)})
    return usersEntity(conn.local.user.find_one({'_id':ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id,user:User):
    return usersEntity(conn.local.user.find_one_and_delete({'_id': ObjectId(id)}))

@user.post('/login_student')
async def login_student(user:Student):
    for current_user in conn.local.user.find():
        print(current_user,user) 
        if current_user['name'] == user['name'] and current_user['password'] == user['password']:
            conn.local.Student.insert_one(dict(user))
            return {'data': dict(current_user)['_id']}
    return {'error':'Invalid credentials'}