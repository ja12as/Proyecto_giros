from fastapi import APIRouter
from sqlalchemy.orm import Session
from api.models.database import engine

router = APIRouter(prefix="/ips", tags=["IPS"])

@router.get("/")
def listar_ips():
    with Session(engine) as session:
        query = session.execute("SELECT * FROM IPS").fetchall()
        return [dict(row) for row in query]