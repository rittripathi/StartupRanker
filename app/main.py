from fastapi import FastAPI
import uuid
from app.schemas import IdeaSubmitRequest, IdeaSubmitResponse
from app.checkpoint import check_idea_validity

app = FastAPI(title="Startup Ranker")

@app.get("/health")
def health_check():
    return {"status": "working"}

@app.post("/ideas", response_model=IdeaSubmitResponse)
def submit_idea(payload:IdeaSubmitRequest):
    idea_id=str(uuid.uuid4())
    is_valid=check_idea_validity(payload.idea_text)
    if not is_valid:
        return IdeaSubmitResponse(
            idea_id=idea_id,
            is_valid=False,
            message="This doesnt appear to be a startup/business idea"
        )
    return IdeaSubmitResponse(
        idea_id=idea_id,
        is_valid=is_valid,
        message="Idea submitted successfully, Evaluating..."
    )