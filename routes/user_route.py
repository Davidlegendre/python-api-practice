from fastapi import APIRouter
from models.SystemReturnModel import SystemReturn
from models.dtos.User_DTO import User_DTO
from services.user_service import get_users, get_one_user, create_user, delete_user, update_user

route = APIRouter(prefix="/users", tags=["users"])

@route.get("/get_users", response_model=SystemReturn) 
async def get_all():
    return await get_users()
    
@route.get("/get_one/{item_id}", response_model=SystemReturn)
async def get_one(item_id: int):
    return await get_one_user(item_id)

@route.post("/create_user",  response_model=SystemReturn)
async def create(item: User_DTO):
    return await create_user(item)

@route.put("/update_user/{item_id}",  response_model=SystemReturn)
async def update(item_id: int, user: User_DTO):
    return await update_user(item_id, user)


@route.delete("/delete_user/{item_id}",  response_model=SystemReturn)
async def delete(item_id: int):
    return await delete_user(item_id)