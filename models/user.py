import datetime
from pydantic import BaseModel 

class User(BaseModel):
    name:str
    password:str
    role:int ### 1=> teacher 0=> student
    
class Student(BaseModel):
    name:str
    systemIP:str
    status:bool
    login_time: str = datetime.datetime.now()
    logout_time:str
    
class Teacher(BaseModel):
    name:str
    systemIP:str
    purpose:str
    status:bool
    login_time:str = datetime.datetime.now()
    logout_time:str

