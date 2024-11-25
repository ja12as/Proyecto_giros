from fastapi import APIRouter
from sqlalchemy.orm import Session
from api.models.database import engine

router = APIRouter(prefix="/eps", tags=["EPS"])

@router.get("/")
def listar_eps():
    with Session(engine) as session:
        query = session.execute("SELECT * FROM EPS").fetchall()
        return [dict(row) for row in query]