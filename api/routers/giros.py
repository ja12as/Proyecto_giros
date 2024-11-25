from fastapi import APIRouter
from sqlalchemy.orm import Session
from api.models.database import engine

router = APIRouter(prefix="/giros", tags=["Giros"])

@router.get("/")
def listar_giros():
    with Session(engine) as session:
        query = session.execute("SELECT * FROM Giros").fetchall()
        return [dict(row) for row in query]
