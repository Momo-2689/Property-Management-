from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.property import Property as PropertyModel
from schemas.property import PropertyCreate, Property

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Property)
def create_property(property: PropertyCreate, db: Session = Depends(get_db)):
    db_property = PropertyModel(**property.dict())
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

@router.get("/", response_model=list[Property])
def list_properties(db: Session = Depends(get_db)):
    return db.query(PropertyModel).all()
