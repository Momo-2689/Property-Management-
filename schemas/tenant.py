from pydantic import BaseModel

class TenantBase(BaseModel):
    name: str
    address: str

class TenantCreate(TenantBase):
    pass

class Tenant(TenantBase):
    id: int

    class Config:
        orm_mode = True