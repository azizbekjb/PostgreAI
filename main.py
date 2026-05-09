from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from dotenv import load_dotenv

# Ilovani o'rnatish
app = FastAPI()

# Statik fayllar va template(html sahifa)larini ulash
app.mount("/static", StaticFiles(directory="static"), "static")
templates = Jinja2Templates(directory="templates")

# Validatsiya uchun sinf yaratish
class ChatRequest(BaseModel):
    message: str

# Kerakli kalitlarni yuklash
load_dotenv()

# Modelni ishga tushurish
model = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")

# Agent yaratish va modelni ulash
agent = create_agent(
    model=model,
    tools=[],
    system_prompt="Sen shunchaki savolga javob ber."
)

# Test uchun funksiya yozish
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(name="agent.html", request=request, context={})

@app.post("/chat")
async def chat(req: ChatRequest):

    resp = agent.invoke({
        "messages": HumanMessage(content=req.message)
    })
    
    if isinstance(resp, dict):
        text = resp["messages"][-1].content
    else:
        text = getattr(resp, "reply", None) or getattr(resp, "text", None) or getattr(resp, "output", None) or str(resp)
    return JSONResponse({"reply": text})
