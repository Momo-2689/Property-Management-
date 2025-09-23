from database import Base, create_engine
from models import property, tenant , maintenance

Base.metadata.create_all(bind=create_engine)