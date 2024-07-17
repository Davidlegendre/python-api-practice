from pydantic import BaseModel

class User_DTO(BaseModel):
    dni: int
    nombre: str
    edad: int