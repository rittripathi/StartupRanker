from fastapi import FastAPI, Depends
import uuid
from sqlalchemy.orm import Session
from app.schemas import IdeaSubmitRequest, IdeaSubmitResponse,IdeaOut
from app.checkpoint import check_idea_validity
from app.evaluator import evaluate_idea
from app.database import get_db
from app.model import Idea
from typing import List

app = FastAPI(title="Startup Ranker")

@app.get("/health")
def health_check():
    return {"status": "working"}

@app.get("/ideas", response_model=List[IdeaOut])
def list_ideas(db: Session=Depends(get_db)):
    ideas=db.query(Idea).order_by(Idea.overall_score.desc()).limit(100).all()
    return ideas

@app.post("/ideas", response_model=IdeaSubmitResponse)
def submit_idea(payload:IdeaSubmitRequest, db: Session=Depends(get_db)):
    idea_id=str(uuid.uuid4())
    is_valid=check_idea_validity(payload.idea_text)
    if not is_valid:
        return IdeaSubmitResponse(
            idea_id=idea_id,
            is_valid=False,
            message="This doesnt appear to be a startup/business idea"
        )
    try :
        score = evaluate_idea(payload.idea_text)
    except Exception as e:
        return IdeaSubmitResponse(
            idea_id=idea_id,
            is_valid=False,
            message="Evaluation failed"
        )

    db_idea=Idea(
        id=idea_id,
        idea_text=payload.idea_text,
        problem_severity=score.problem_severity,
        market_size=score.market_size,
        customer_demand=score.customer_demand,
        unique_insight=score.unique_insight,
        competitive_moat=score.competitive_moat,
        market_timing=score.market_timing,
        business_model=score.business_model,
        scalability=score.scalability,
        execution_difficulty=score.execution_difficulty,
        summary=score.summary,
        overall_score=score.overall_score,
    )
    db.add(db_idea)
    db.commit()
    return IdeaSubmitResponse(
        idea_id=idea_id,
        is_valid=is_valid,
        message="Idea submitted successfully, Evaluating...",
        score=score
    )