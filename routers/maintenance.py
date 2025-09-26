from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.maintenance import Maintenance as MaintenanceModel
from schemas.maintenance import MaintenanceCreate, Maintenance

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Maintenance)
def create_maintenance(ticket: MaintenanceCreate, db: Session = Depends(get_db)):
    db_ticket = MaintenanceModel(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@router.get("/", response_model=list[Maintenance])
def list_maintenance(db: Session = Depends(get_db)):
    return db.query(MaintenanceModel).all()
