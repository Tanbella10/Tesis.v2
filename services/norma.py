from models.norma import Norma as Normamodel
from schemas.norma import Norma

class NormaService():
    
  #Metodo consultor init
    def __init__(self, db) -> None:
        self.db = db

    #creacion del primer metodo
    def get_normas(self):
        result = self.db.query(Normamodel).all()
        return result

    def get_norma(self, id:int):
        result = self.db.query(Normamodel).filter(Normamodel.id == id).first()
        return result

    
    def get_norma_cat(self, category):
        result = self.db.query(Normamodel).filter(Normamodel.category == category).all()
        return result

    #creacion de un nuevo metodo 
    def create_normas(self, norma: Norma):
        new_norma = Normamodel(**norma.dict())
        self.db.add(new_norma)
        self.db.commit()
        return

        