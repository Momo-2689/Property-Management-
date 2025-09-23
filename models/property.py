from sqlalchemy import Column, Integer, String
from database import Base

class property(Base):
    __tablename__ = "property"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
