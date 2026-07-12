from groq import Groq
from app.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def call_llm(prompt:str) ->str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{
            "role":"user",
            "content": prompt
        }],
        temperature=0.2
    )
    return response.choices[0].message.content