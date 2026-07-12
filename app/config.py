import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set")

CRITERIA_WEIGHTS = {
    "problem_severity": 22,
    "market_size": 18,
    "customer_demand": 15,
    "unique_insight": 12,
    "competitive_moat": 10,
    "market_timing": 8,
    "business_model": 7,
    "scalability": 5,
    "execution_difficulty": 3,
}