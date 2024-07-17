from models.SystemReturnModel import SystemReturn
from models.User import User_Model
from utils.utils import get_item


user_bd: list[User_Model] = list()

async def get_users() -> SystemReturn:
    if (len(user_bd) == 0):
        return SystemReturn(mensaje="no hay usuarios")
    else:
        return SystemReturn(mensaje="usuarios", data=user_bd)

async def get_one_user(item_id: int) -> SystemReturn:
    if len(user_bd) == 0: return  SystemReturn(mensaje="no hay datos") 
    usuario = get_item(item_id, user_bd=user_bd)
    if usuario: return SystemReturn(mensaje="usuario", data=usuario)    
    return SystemReturn(mensaje="ese id no existe")


async def create_user(item: User_Model) -> SystemReturn:
    result = False
    user = get_item(item.id, user_bd)
    if user: return SystemReturn(mensaje=f"ese usuario ya existe con ese id: {item.id}")
    user_bd.append(item)
    return SystemReturn(mensaje="usuario agregado", data=item)

async def update_user(id_item: int, item: User_Model) -> SystemReturn:
    if len(user_bd) == 0: return  SystemReturn(mensaje="no hay datos") 
    user = get_item(id_item, user_bd)  
    if user:
        user.nombre = item.nombre
        user.edad = item.edad
        user.money = item.money
        return SystemReturn(mensaje="usuario modificado", data=user) 
    return SystemReturn(mensaje="ese id no existe")  

async def delete_user(id_item: int) -> SystemReturn:
    if len(user_bd) == 0: return SystemReturn(mensaje="no hay datos")
    user = get_item(id_item, user_bd)
    if user:
        user_bd.remove(user)
        return SystemReturn(mensaje=f"Usuario {user.nombre} Eliminado", data=user)
    return SystemReturn(mensaje="ese id no existe") 