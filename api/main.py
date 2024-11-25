from fastapi import FastAPI
from .models.database import engine, Base
from .routers import eps, ips, giros, ubicacion

app = FastAPI()

# Importar los modelos para registrarlos con el Base
from .models import eps, ips, giros, ubicacion

# Crear tablas
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(eps.router)
app.include_router(ips.router)
app.include_router(giros.router)
app.include_router(ubicacion.router)
