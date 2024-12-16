from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#crear entidad

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

user_list = [User(id= 1,name = "Oscar",surname = "Becerril",url= "www.oscar.com",age=49),
             User(id= 2,name = "Laura",surname = "Navarrete",url= "www.Laura.com",age=41),
             User(id= 3,name = "Pepe",surname = "Becerril",url= "www.pepe.com",age=49)]

@app.get("/usersjson")
async def userjson():
    return [{"name" : "Oscar", "surname" : "Becerril", "url" : "www.oscar.com", "age" : 49}]

@app.get("/users")
async def users():
    return user_list

@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#para arrancar el server uvicorn.exe users:app --reload

@app.get("/userquery/*")
async def userquery(id: int):
    return search_user(id)

@app.post("/user/*")
async def user(user: User):
    user_list.append (user)

def search_user(id: int):
    users = filter (lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"error" : "Usuario no existe"}   