from pydantic import BaseModel, Field

class IdeaSubmitRequest(BaseModel):
    idea_text: str = Field(..., min_length=20,max_length=3000)

class IdeaSubmitResponse(BaseModel):
    idea_id: str
    is_valid: bool
    message: str

class IdeaScore(BaseModel):
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