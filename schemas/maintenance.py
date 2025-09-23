from pydantic import BaseModel

class MaintenanceBase(BaseModel):
    name: str
    address: str

class MaintenanceCreate(MaintenanceBase):
    pass

class Maintenance(MaintenanceBase):
    id: int

    class Config:
        orm_mode = True