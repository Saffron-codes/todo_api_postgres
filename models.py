from pydantic import *

class User(BaseModel):
    # user_id:int
    name:str
    email:str
    password:str
    class Config:
        orm_mode: True

class Todo(BaseModel):
    # id:int
    description:str
    user_id:int
    class Config:
        orm_mode: True


class TodoIn(BaseModel):
    id:int
    new_description:str
    user_id:int
    class Config:
        orm_mode: True