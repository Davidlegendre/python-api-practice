from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import starlette.status as status
from routes import user_route, todo_route
from database.mongo import client

app = FastAPI()
@app.get("/")
async def default_root():
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)

app.include_router(user_route.router)
app.include_router(todo_route.router)