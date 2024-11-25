from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurar la conexión al motor de PostgreSQL
DATABASE_URL = "postgresql://postgres:root@localhost/giros_db"

engine = create_engine(DATABASE_URL, echo=True)

# MetaData y Base para definir los modelos
metadata = MetaData()
Base = declarative_base()

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
