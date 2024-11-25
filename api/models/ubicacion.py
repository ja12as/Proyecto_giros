from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from .database import Base
from .giros import Giros

class Ubicacion(Base):
    __tablename__ = "Ubicacion"

    DANE = Column(String(10), primary_key=True)
    Departamento = Column(String(255), nullable=True)
    Municipio = Column(String(255), nullable=True)

    giros = relationship("Giros", back_populates="ubicacion")
