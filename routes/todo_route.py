from fastapi import APIRouter
from database.mongo import client
from utils.utils import MONGO_DB
from models.SystemReturnModel import SystemReturn

router = APIRouter(prefix="/Todo", tags=["Todo"])

@router.get("/", response_model=SystemReturn)
async def get_todos() -> SystemReturn:
    collection = client["TodoBD"].get_collection("Todos").find({})
    data = []
    for c in collection:
        data.append({"_id": str(c["_id"]), "User": c["User"]})
    return SystemReturn(mensaje="Todos", data=data)