from pydantic import BaseModel
class User_Model(BaseModel):
    id: int
    dni: int
    nombre: str
    edad: int