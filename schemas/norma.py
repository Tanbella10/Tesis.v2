from pydantic import BaseModel
from typing import Optional



#Creación del esquema de datos
class Norma(BaseModel):
    id: Optional[int] = None
    category: str
    title: str
    subCategory: str
    year:int
    vigencia:bool
    Resumen:str
    link:str



