from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from database import SessionLocal
from models.tenant import Tenant as tenantModel
from schemas.tenant import TenantCreate, Tenant

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Tenant)
def create_tenant(tenant: TenantCreate, db: Session = Depends(get_db)):
    db_tenant = tenantModel(**tenant.dict())
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant

@router.get("/", response_model=list[Tenant])
def list_properties(db: Session = Depends(get_db)):
    return db.query(tenantModel).all()