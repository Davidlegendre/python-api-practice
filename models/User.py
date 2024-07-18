from pydantic import BaseModel
class User_Model(BaseModel):
    id: str
    dni: int
    nombre: str
    edad: int