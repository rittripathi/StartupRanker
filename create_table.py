from app.database import Base, engine
from app.model import Idea

Base.metadata.create_all(bind=engine)
print("Tables created successfully.")