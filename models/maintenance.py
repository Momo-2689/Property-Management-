from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from database import Base

class Maintenance(Base):
    __tablename__ = 'maintenance'

    id = Column(Integer, primary_key=True, index=True)
    issue = Column(String)
    Status = Column(String, default="pending")
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    property_id = Column(Integer, ForeignKey("properties.id"))