from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import properties, tenant, maintenance
from database import Base, engine
from models import property, tenant, maintenance as maintenance_model

app = FastAPI()

app.add_middleware(

CORSMiddleware,
allow_oringins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(properties.router, prefix="/api/properties", tags=["Properties"])
app.include_router(tenant.router, prefix="/apimaintance", tags=["Maintenance"])
app.include_router(maintenance.router, prefix="/api/maintenance", tags=["Maintenance"])

@app.get("/")
def root():
    return {"message": "Landlord Property Management Backend is running..."}