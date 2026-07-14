import json
from app.llm_client import call_llm
from app.schemas import IdeaScoreParameters
from app.config import CRITERIA_WEIGHTS

EVALUATION_PROMPT="""
You are a startup idea evaluator. Score the idea below on each criterion from 1-10.
respond IN ONLY VALID JSON  no other text not even a coma outside json format response exactly like this :
{{
    "problem_severity":<int 1-10>,
    "market_size": <int 1-10>,
    "customer_demand": <int 1-10>,
    "unique_insight": <int 1-10>,
    "competitive_moat": <int 1-10>,
    "market_timing": <int 1-10>,
    "business_model": <int 1-10>,
    "scalability": <int 1-10>,
    "execution_difficulty": <int 1-10>,
    "summary": "<short analysis not more than 2 lines>"
}}
IDEA:
\"\"\{idea_text}\"\"\"
"""

def calculate_overall_score(scores:dict)->float:
    total_weight=sum(CRITERIA_WEIGHTS.values())
    weighted_sum=sum(
        scores[criterion]*weight
        for criterion,weight in CRITERIA_WEIGHTS.items()
    )
    return round(weighted_sum/total_weight, 2)

def evaluate_idea(idea_text:str)->IdeaScoreParameters:
    prompt=EVALUATION_PROMPT.format(idea_text=idea_text)
    raw_response=call_llm(prompt)
    data=json.loads(raw_response)
    idea_score= IdeaScoreParameters(**data)
    idea_score.overall_score= calculate_overall_score(data)
    return idea_score
    