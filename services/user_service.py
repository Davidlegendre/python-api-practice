from models.SystemReturnModel import SystemReturn
from models.User import User_Model
from models.dtos.User_DTO import User_DTO
from fastapi import HTTPException,status
from messages import messages
from bson import ObjectId

from database.mongo import client
from utils.utils import MONGO_DB

async def get_users() -> SystemReturn:
    count = client[MONGO_DB].get_collection("Users").count_documents({})           
    if (count == 0): raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.NoHayUsuarios)
    
    collection = client[MONGO_DB].get_collection("Users").find({})
    data: list[User_Model] = list()
    for c in collection:
        data.append(User_Model(id=str(c["_id"]), dni=c["dni"], nombre=c["nombre"], edad=c["edad"]))
        
    return SystemReturn(mensaje=messages.Usuarios, data=data)

async def get_one_user(item_id: str) -> SystemReturn:
    #buscar cuantos documentos hay
    count = client[MONGO_DB].get_collection("Users").count_documents({})
    if count == 0: raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.NoHayDatos)    
    usuario = client[MONGO_DB].get_collection("Users").find_one({"_id": ObjectId(item_id)})
    if not usuario:  raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.EseIdNoExiste)
    return SystemReturn(mensaje=messages.Usuario, data=User_Model(id=str(usuario["_id"]), dni=usuario["dni"], nombre=usuario["nombre"], edad=usuario["edad"]))    
   

#Recibe un DTO y lo guarda en Modelo
async def create_user(item: User_DTO) -> SystemReturn:    
    user = client[MONGO_DB].get_collection("Users").find_one({"dni": item.dni})
    if user: raise HTTPException(status.HTTP_409_CONFLICT, detail=messages.UsuarioYaExiste)   
    id = str(client[MONGO_DB].get_collection("Users").insert_one(item.model_dump()).inserted_id)
    return SystemReturn(mensaje=f"{messages.Usuario} {messages.Agregado}", data=User_Model(id=id, dni=item.dni, nombre=item.nombre, edad=item.edad))

#Modifica desde un DTO a Model
async def update_user(id_item: str, item: User_DTO) -> SystemReturn:
    #buscar cuantos documentos hay
    count = client[MONGO_DB].get_collection("Users").count_documents({})
    if count == 0: raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.NoHayDatos)
    #buscar si existe ese id
    object_id = ObjectId(id_item)
    
    user = client[MONGO_DB].get_collection("Users").find_one({"_id": object_id})
    if not user: raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.EseIdNoExiste)
    #actualizar el item
    update_data = {k: v for k, v in item.model_dump().items() if v is not None}
    
    result = client[MONGO_DB].get_collection("Users").update_one({"_id" : object_id}, {"$set": update_data}).modified_count
    
    if result == 0: raise HTTPException(status.HTTP_304_NOT_MODIFIED, detail=f"{messages.Usuario} no {messages.Modificado}")
    
    user = client[MONGO_DB].get_collection("Users").find_one({"_id": object_id})
    
    return SystemReturn(mensaje=f"{messages.Usuario} {messages.Modificado}", data=User_Model(id=id_item, dni=user["dni"], nombre=user["nombre"], edad=user["edad"]))
   

async def delete_user(id_item: str) -> SystemReturn:
    #buscar cuantos documentos hay
    count = client[MONGO_DB].get_collection("Users").count_documents({})
    if count == 0: raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.NoHayDatos)
    object_id = ObjectId(id_item)
    
    user = client[MONGO_DB].get_collection("Users").find_one({"_id": object_id})
    if not user: raise HTTPException(status.HTTP_404_NOT_FOUND, detail=messages.EseIdNoExiste)
    
    result = client[MONGO_DB].get_collection("Users").delete_one({"_id": object_id}).deleted_count
    if(result == 0): raise HTTPException(status.HTTP_304_NOT_MODIFIED, detail=SystemReturn(mensaje=f"{messages.Usuario} no {messages.Eliminado}"))
    return SystemReturn(mensaje=f"{messages.Usuario} {user["nombre"]} {messages.Eliminado}", data=User_Model(id=id_item, dni=user["dni"], nombre=user["nombre"], edad=user["edad"]))