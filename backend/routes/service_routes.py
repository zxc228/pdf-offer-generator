from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.service import Service
from schemas.service import ServiceCreate, ServiceRead

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/services", response_model=list[ServiceRead])
def read_services(db: Session = Depends(get_db)):
    return db.query(Service).all()


