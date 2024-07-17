from models.SystemReturnModel import SystemReturn
from models.User import User_Model
from models.dtos.User_DTO import User_DTO
from utils.utils import get_item_byDNI, get_item_byId
from fastapi import HTTPException,status, encoders
from messages import messages

user_bd: list[User_Model] = list()

def setCount() -> int:
    if len(user_bd) == 0: return 1
    return user_bd[len(user_bd) - 1].id + 1

async def get_users() -> SystemReturn:
    if (len(user_bd) == 0):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.NoHayUsuarios)
    else:
        return SystemReturn(mensaje=messages.Usuarios, data=user_bd)

async def get_one_user(item_id: int) -> SystemReturn:
    if len(user_bd) == 0: raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.NoHayUsuarios)
    usuario = get_item_byId(item_id, user_bd=user_bd)
    if usuario: return SystemReturn(mensaje=messages.Usuario, data=usuario)    
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.EseIdNoExiste)

#Recibe un DTO y lo guarda en Modelo
async def create_user(item: User_DTO) -> SystemReturn:
    user = get_item_byDNI(item.dni, user_bd)
    if user: raise HTTPException(status.HTTP_409_CONFLICT, detail=messages.UsuarioYaExiste)   
    user_bd.append(User_Model(id=setCount(), dni=item.dni, nombre=item.nombre, edad=item.edad))
    return SystemReturn(mensaje=f"{messages.Usuario} {messages.Agregado}", data=item)

#Modifica desde un DTO a Model
async def update_user(id_item: int, item: User_DTO) -> SystemReturn:
    if len(user_bd) == 0: raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.NoHayDatos)
    user = get_item_byId(id_item, user_bd)
    if user:
        user.nombre = item.nombre
        user.edad = item.edad
        user.dni = item.dni
        return SystemReturn(mensaje=f"{messages.Usuario} {messages.Modificado}", data=user) 
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.EseIdNoExiste)

async def delete_user(id_item: int) -> SystemReturn:
    if len(user_bd) == 0: raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.NoHayDatos)
    user = get_item_byId(id_item, user_bd)
    if user:
        user_bd.remove(user)
        return SystemReturn(mensaje=f"{messages.Usuario} {user.nombre} {messages.Eliminado}", data=user)
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.EseIdNoExiste)