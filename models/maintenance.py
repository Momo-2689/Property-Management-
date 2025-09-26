from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Maintenance(Base):
    __tablename__ = "maintenance"
    id = Column(Integer, primary_key=True, index=True)
    issue = Column(String)
    status = Column(String, default="Pending")
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    property_id = Column(Integer, ForeignKey("properties.id"))
