from pydantic import BaseModel
class SystemReturn(BaseModel):
    mensaje: str
    data: object = None
    