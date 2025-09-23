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
def create_Maintenance(Maintenance: MaintenanceCreate, db: Session = Depends(get_db)):
    db_Maintenance = MaintenanceModel(**Maintenance.dict())
    db.add(db_Maintenance)
    db.commit()
    db.refresh(db_Maintenance)
    return db_Maintenance

@router.get("/", response_model=list[Maintenance])
def list_properties(db: Session = Depends(get_db)):
    return db.query(MaintenanceModel).all()