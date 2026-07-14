from sqlalchemy import Column, String, Integer, Float, DateTime, ARRAY, Boolean
from sqlalchemy.sql import func
from app.database import Base

class Idea(Base):
    __tablename__ ="ideas"
    id = Column(String, primary_key=True, index= True)
    idea_text=Column(String, nullable=True)
    problem_severity = Column(Integer)
    market_size = Column(Integer)
    customer_demand = Column(Integer)
    unique_insight = Column(Integer)
    competitive_moat = Column(Integer)
    market_timing = Column(Integer)
    business_model = Column(Integer)
    scalability = Column(Integer)
    execution_difficulty = Column(Integer)

    summary = Column(String)
    overall_score= Column(Float)
    created_at = Column(DateTime(timezone=True),server_default=func.now())

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
