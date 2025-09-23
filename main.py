from database import Base, engine
from models import property, tenant , maintenance

Base.metadata.create_all(bind=engine)