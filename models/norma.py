from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Norma(Base):

    __tablename__ = "normas"
    id = Column(Integer, primary_key = True)
    category = Column (String)
    title = Column (String)
    subCategory = Column (String)
    year = Column (Integer)
    vigencia = Column (Boolean)
    Resumen = Column (String)
    link = Column (String)

