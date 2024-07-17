from typing import Union

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from models.User import User_Model
from models.SystemReturnModel import SystemReturn
import starlette.status as status

app = FastAPI()

user_bd: list[User_Model] = list()

@app.get("/")
async def default_root():
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)

@app.get("/get_users") 
async def get_users() -> SystemReturn:
    if (len(user_bd) == 0):
        return SystemReturn(mensaje="no hay usuarios")
    else:
        return SystemReturn(mensaje="usuarios", data=user_bd)
    
@app.get("/get_one/{item_id}")
async def get_one_user(item_id: int) -> SystemReturn:
    if len(user_bd) == 0: return  SystemReturn(mensaje="no hay datos") 
    for user in user_bd:
       if(user.id == item_id):
           return SystemReturn(mensaje="usuario", data=user)
    return SystemReturn(mensaje="ese id no existe")
    
           

@app.post("/create_user")
async def create_user(item: User_Model) -> SystemReturn:
    result = False
    for user in user_bd:
        if user.id == item.id:
            return SystemReturn(mensaje=f"ese usuario ya existe con ese id: {item.id}")
    user_bd.append(item)
    return SystemReturn(mensaje="usuario agregado", data=item)

@app.put("/update_user/{id_item}")
async def update_user(item: User_Model, id_item: int) -> SystemReturn:
    if len(user_bd) == 0: return  SystemReturn(mensaje="no hay datos") 
    for indice, usuario in enumerate(user_bd):
        if usuario.id == id_item:            
            user = user_bd[indice]
            user.nombre = item.nombre
            user.edad = item.edad
            user.money = item.money
            return SystemReturn(mensaje="usuario modificado", data=user_bd[indice]) 
    return SystemReturn(mensaje="ese id no existe")  

@app.delete("/delete_user/{item_id}")
async def delete_user(id_item: int) -> SystemReturn:
    if len(user_bd) == 0: return SystemReturn(mensaje="no hay datos")
    for usuario in user_bd:
        if(usuario.id == id_item):
            user = usuario
            user_bd.remove(usuario)
            return SystemReturn(mensaje=f"Usuario {user.nombre} Eliminado", data=user)
    return SystemReturn(mensaje="ese id no existe")  
