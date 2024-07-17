from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import starlette.status as status
from models.User import User_Model
from services.user_service import get_users, get_one_user, create_user, delete_user, update_user


app = FastAPI()

@app.get("/")
async def default_root():
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)

@app.get("/get_users") 
async def get_all():
    return await get_users()
    
@app.get("/get_one/{item_id}")
async def get_one(item_id: int):
    return await get_one_user(item_id)

@app.post("/create_user")
async def create(item: User_Model):
    return await create_user(item)

@app.put("/update_user/{item_id}")
async def update(item_id: int, user: User_Model):
    return await update_user(item_id, user)


@app.delete("/delete_user/{item_id}")
async def delete(item_id: int):
    return await delete_user(item_id)