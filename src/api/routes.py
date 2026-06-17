# src/api/routes.py
from fastapi import APIRouter 
from pydantic import BaseModel, Field
from src.llm.llm_client import gemini_agent 

router = APIRouter() # app emas router deb nomlang

class AgentRequest(BaseModel):
    question: str = Field(
        max_length=500,
        description="Foydalanuvchi bergan savoli"
    )
    
@router.post("/answer")
async def answer(request: AgentRequest):
    question = request.question
    ai_response = gemini_agent(user_query=question)

    return {"answer": ai_response}