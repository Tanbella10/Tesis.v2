from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional
from config.database import Session, engine, Base
from models.norma import Norma as Normamodel
from fastapi.encoders import jsonable_encoder
from routers.norma import norma_router
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

app = FastAPI()
app.title = "Cracks"
app.version = "0.0.1"

print(config('FRONTEND_URL'))

origins = [
	config('FRONTEND_URL')
]

app.add_middleware(
	CORSMiddleware,
	allow_origins= origins,
	allow_credentials=True,
	allow_methods = ['*'],
	allow_headers = ['*']
)


app.include_router(norma_router)

Base.metadata.create_all(bind= engine)




normas = [
    {
		"id": 1,
		"title": "Catastro Multiprosposito",
		"category": "ley",
		"year": "2009",
		"vigencia": True,
		"Resumen": "esta ley se trata de ----",
        "link": "link"
	},
     {
		"id": 2,
		"title": "Catastro Multiprosposito",
		"category": "norma",
		"year": "2009",
		"vigencia": True,
		"Resumen": "esta ley se trata de ----",
        "link": "link"
	}
]


@app.get('/', tags=["HOME"] )
def mensage ():
    return HTMLResponse('<h1>Acceso administración plataforma de consulta de normativa catastral!</h1>' "<h2> Cracks </h2>")

