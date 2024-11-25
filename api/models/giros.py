from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Giros(Base):
    __tablename__ = "Giros"

    IDGiro = Column(Integer, primary_key=True, autoincrement=True)
    DANE = Column(String(10), ForeignKey("Ubicacion.DANE"))
    CodiEPS = Column(String(10), ForeignKey("EPS.CodiEPS"))
    NITIPS = Column(String(15), ForeignKey("IPS.NITIPS"))
    FormaContratacion = Column(String(255))
    TotalGiro = Column(DECIMAL(20, 2))
    TipoGiro = Column(String(50))
    Observaciones = Column(Text)

    ubicacion = relationship("Ubicacion", back_populates="giros")
    eps = relationship("EPS", back_populates="giros")
    ips = relationship("IPS", back_populates="giros")
