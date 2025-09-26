from pydantic import BaseModel

class TenantBase(BaseModel):
    name: str
    email: str
    phone: str
    property_id: int

class TenantCreate(TenantBase):
    pass

class Tenant(TenantBase):
    id: int

    class Config:
        orm_mode = True
