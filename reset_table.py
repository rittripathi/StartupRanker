from app.database import Base, engine
from app.model import Idea

Base.metadata.drop_all(bind=engine)
print("Tables dropped.")

Base.metadata.create_all(bind=engine)
print("Tables recreated.")