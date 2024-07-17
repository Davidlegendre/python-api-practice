from pydantic import BaseModel
class User_Model(BaseModel):
    id: int
    nombre: str
    edad: int
    money: float