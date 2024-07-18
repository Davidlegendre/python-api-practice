from fastapi import APIRouter
from models.SystemReturnModel import SystemReturn
from models.dtos.User_DTO import User_DTO
from services.user_service import get_users, get_one_user, create_user, delete_user, update_user


router = APIRouter(prefix="/users", tags=["users"])

@router.get("/get_users", response_model=SystemReturn) 
async def get_all():
    return await get_users()
    
@router.get("/get_one/{item_id}", response_model=SystemReturn)
async def get_one(item_id: str):
    return await get_one_user(item_id)

@router.post("/create_user",  response_model=SystemReturn)
async def create(item: User_DTO):
    return await create_user(item)

@router.put("/update_user/{item_id}",  response_model=SystemReturn)
async def update(item_id: str, user: User_DTO):
    return await update_user(item_id, user)


@router.delete("/delete_user/{item_id}",  response_model=SystemReturn)
async def delete(item_id: str):
    return await delete_user(item_id)