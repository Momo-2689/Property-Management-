from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    property_id = Column(Integer, ForeignKey("properties.id"))
