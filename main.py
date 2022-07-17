from distutils.util import execute
from fastapi import FastAPI, HTTPException, status
from soupsieve import select
from database import *
from schemas import *
from models import Todo, TodoIn, User
app = FastAPI()



@app.on_event("startup")
async def startup():
    await database.connect()
    print("Connected to Database!")

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    print("Disonnected to Database!")



@app.get('/')
async def home():
    return "Hello World";

@app.get('/favicon.ico')
async def home():
    return "Hello World";

@app.post('/register')
async def Register(user:User):
    query = users.insert().values(name=user.name,email=user.email,password=user.password);
    try:
        result = await database.execute(query)
        print(result);
        return user
    except Exception as e:
        error = e
        print(error.args)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=error.args)
    return result





@app.get('/notes')
async def getTodos(user_id:int):
    userTodos = []
    query = "select id,description from users inner join todos on users.user_id = {s} and todos.user_id = {s}".format(s=user_id)
    # print(query)
    results =  conn.execute(query)
    for rows in results:
        userTodos.append({"id":rows[0],"description":rows[1]})
    return userTodos




@app.post('/notes/create')
async def addTodos(todo:Todo):
    query = todos.insert().values(description=todo.description,user_id=todo.user_id)
    try:
        result = await database.execute(query)
        print(result);
        return todo
    except Exception as e:
        error = e
        print(error.args)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=error.args)
    return result


@app.put('/notes/update')
async def updateTodos(todo:TodoIn):
    query = todos.update().where(todos.c.id == todo.id and todos.c.user_id == todo.user_id).values(description=todo.new_description)
    try:
        result = await database.execute(query)
        return todo
    except Exception as e:
        error = e
        print(error.args)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=error.args)




@app.delete('/notes/delete')
async def updateTodos(id:int,user_id:int):
    query = todos.delete().where(todos.c.id == id and todos.c.user_id == user_id)
    try:
        result = await database.execute(query)
        return {"message":"deleted"}
    except Exception as e:
        error = e
        print(error.args)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=error.args)

    

