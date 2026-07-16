from pydantic import BaseModel, Field
from datetime import datetime
class IdeaSubmitRequest(BaseModel):
    idea_text: str = Field(..., min_length=20,max_length=3000)


class IdeaScoreParameters(BaseModel):
    problem_severity: int = Field(..., ge=1, le=10)
    market_size: int = Field(..., ge=1, le=10)
    customer_demand: int = Field(..., ge=1, le=10)
    unique_insight: int = Field(..., ge=1, le=10)
    competitive_moat: int = Field(..., ge=1, le=10)
    market_timing: int = Field(..., ge=1, le=10)
    business_model: int = Field(..., ge=1, le=10)
    scalability: int = Field(..., ge=1, le=10)
    execution_difficulty: int = Field(..., ge=1, le=10)
    summary: str
    overall_score: float = 0.0    

class IdeaOut(BaseModel):
    id: str
    idea_text: str
    overall_score: float
    summary:str
    created_at:datetime

    class Config:
        from_attributes=True

class IdeaSubmitResponse(BaseModel):
    idea_id: str
    is_valid: bool
    message: str
    score: IdeaScoreParameters|None=None

class UserSignup(BaseModel):
    email: str
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    email:str
    password:str

class UserOut(BaseModel):
    id:str
    email:str

    class Config:
        from_attributes = True
        