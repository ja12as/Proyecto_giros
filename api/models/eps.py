
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from .database import Base

class EPS(Base):
    __tablename__ = "EPS"

    CodiEPS = Column(String(10), primary_key=True)
    NombreEPS = Column(String(255), nullable=False)

    giros = relationship("Giros", back_populates="eps")
