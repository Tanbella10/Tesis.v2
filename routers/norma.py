from fastapi import APIRouter
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional
from config.database import Session, engine, Base
from models.norma import Norma as Normamodel
from fastapi.encoders import jsonable_encoder
from services.norma import NormaService
from schemas.norma import Norma


norma_router = APIRouter()


@norma_router.get('/normas', tags=["NORMA"] )
def getNorma():
    db = Session()
    result = NormaService(db).get_normas()
    #result = db.query(Normamodel).all()
    return JSONResponse (content= jsonable_encoder(result))

@norma_router.get('/normas/{id}', tags=['NORMA'])#para optener las normas por id
def get_Norma(id: int):
    db = Session ()
    result_id = NormaService(db).get_norma(id)
    #result_id = db.query(Normamodel).filter(Normamodel.id == id).first()
    if not result_id:
        return JSONResponse(content={"mensaje": "no se encontro el resultado"})
    #for item in normas:
     #   if item["id"] == id:
      #      return item
    return JSONResponse (content=jsonable_encoder(result_id))

@norma_router.get('/normas/', tags=['NORMA'])#para optener las normas por categoria y año
def get_normas_by_category(category: str):
    db = Session()
    result = NormaService(db).get_norma_cat(category)
    #result = db.query(Normamodel).filter(Normamodel.category == category).all()
    #data = [ item for item in normas if item['category'] == category ]
    return JSONResponse (content= jsonable_encoder(result))

@norma_router.post('/normas', tags=['NORMA'])#para registrar una norma, ley o concept
def create_normas(norma: Norma):
    db = Session()
    NormaService(db).create_normas(norma)
    return JSONResponse(content={"message": "Se ha registrado elemento"})
"""     new_norma = Normamodel(**norma.dict())
    db.add(new_norma)
    db.commit() """
    #normas.append(norma)
    

@norma_router.put('/normas/{id}',tags=['NORMA'])
def update_norma(id: int, norma: Norma):
    db = Session()
    result=db.query(Normamodel).filter(Normamodel.id == id).first()
    if not result:
        return JSONResponse(content={"mensaje": "no se encontro el resultado"})
    result.categoria = norma.category
    result.title = norma.title
    result.subCategory = norma.subCategory
    result.year = norma.year
    result.vigencia = norma.vigencia
    result.Resumen = norma.Resumen
    result.link = norma.link
    db.commit()
    return JSONResponse(content={"mensaje": "Se ha modificado"})

"""     for i in normas:
        if i["id"] == id:
            i["category"] = norma.category
            i["title"] = norma.title
            i["subCategory"] = norma.subCategory
            i["year"] = norma.year
            i["vigencia"] = norma.vigencia
            i["Resumen"] = norma.Resumen
            i["link"] = norma.link
            return JSONResponse(content={"message": "Se ha modificado el elemento"}) """

@norma_router.delete('/normas/{id}', tags=['NORMA'], response_model=dict, status_code=200)
def delete_normas(id: int)-> dict:
    db = Session()
    result=db.query(Normamodel).filter(Normamodel.id == id).first()
    if not result:
        return JSONResponse(content={"mensaje": "no se encontro el resultado"}, status_code=404)
    db.delete(result)
    return JSONResponse(content={"mensaje": "El elemento se ha eliminado"}, status_code=200)
