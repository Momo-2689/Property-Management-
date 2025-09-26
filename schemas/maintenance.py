from pydantic import BaseModel

class MaintenanceBase(BaseModel):
    issue: str
    tenant_id: int
    property_id: int

class MaintenanceCreate(MaintenanceBase):
    pass

class Maintenance(MaintenanceBase):
    id: int
    status: str

    class Config:
        orm_mode = True
