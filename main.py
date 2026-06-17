import uvicorn
from fastapi import FastAPI
from src.api.routes import router # Routerni import qilish
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="PostgreSQL RAG AI")

# Routerni ulash
app.include_router(router)

if __name__ == "__main__":
    # Serverni ishga tushirish
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)