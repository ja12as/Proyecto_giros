from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from .database import Base
from .giros import Giros

class IPS(Base):
    __tablename__ = "IPS"

    NITIPS = Column(String(15), primary_key=True)
    NombreIPS = Column(String(255), nullable=False)

    giros = relationship("Giros", back_populates="ips")
