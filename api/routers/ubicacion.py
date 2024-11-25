from fastapi import APIRouter
from sqlalchemy.orm import Session
from api.models.database import engine

router = APIRouter(prefix="/ubicacion", tags=["Ubicacion"])

@router.get("/")
def listar_ubicacion():
    with Session(engine) as session:
        query = session.execute("SELECT * FROM Ubicacion").fetchall()
        return [dict(row) for row in query]
