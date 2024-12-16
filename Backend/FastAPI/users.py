from fastapi import FastAPI, HTTPException
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


#JSON DE UN SOLO VALOR
@app.get("/usersjson")
async def userjson():
    return [{"name" : "Oscar", "surname" : "Becerril", "url" : "www.oscar.com", "age" : 49}]


#LISTADO DE USERS
@app.get("/users")
async def users():
    return user_list

#BUSCAR USUARIO POR ID
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)
    

#AÑADIR UN USER
@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"Error" : "El usuario ya existe"}
    else:
        user_list.append (user)




def search_user(id: int):
    usersearch = filter (lambda user: user.id == id, user_list)
    try:
        return list(usersearch)[0]
    except IndexError:
        return {"error" : "Usuario no existe"} 
