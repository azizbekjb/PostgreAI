# 🐘 PostgreAI - Intelligent PostgreSQL Assistant

> PostgreSQL rasmiy hujjatlari asosida qurilgan, aqlli qidiruv va javob berish tizimi (RAG)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688.svg)](https://fastapi.tiangolo.com)
[![Google Gemini](https://img.shields.io/badge/AI-Gemini--2.5--Flash-Lite_blueviolet.svg)](https://aistudio.google.com/)

---

## 📋 Mundarija

- [Umumiy ko'rinish](#-umumiy-ko-rinish)
- [Xususiyatlar](#-xususiyatlar)
- [Arxitektura](#-arxitektura)
- [Tezkor boshlash](#-tezkor-boshlash)
- [API Hujjatlar](#-api-hujjatlar)
- [Loyiha strukturasi](#-loyiha-strukturasi)

---

## 🎯 Umumiy ko'rinish

**PostgreAI** — bu PostgreSQL ma'lumotlar bazasining rasmiy hujjatlari (450+ mavzu) asosida yaratilgan Retrieval-Augmented Generation (RAG) tizimi. U foydalanuvchi savollariga faqat tasdiqlangan texnik manbalar asosida aniq javob qaytaradi va har bir javobga manba (URL) ilova qiladi.

**Hozirgi holat:**
- ✅ 47 ta JSON ma'lumotlar to'plami
- ✅ 470+ texnik mavzular indekslangan
- ✅ Semantik qidiruv tizimi tayyor
- ✅ Web-interfeys integratsiya qilingan

---

## ✨ Xususiyatlar

| Xususiyat | Tavsif |
|---------|-------------|
| 🔍 **Semantik Qidiruv** | Kalit so'zlar emas, balki ma'no bo'yicha qidiruv (HuggingFace Embeddings) |
| ⚡ **Tezkor Javob** | Google Gemini 1.5 Flash modeli orqali yuqori tezlikda javob generatsiyasi |
| 📚 **Manba Ko'rsatish** | Har bir javob PostgreSQL rasmiy URL manzillari bilan ta'minlanadi |
| 🐳 **Docker Ready** | Konteynerlashtirilgan va deployga tayyor holat |

---

## 🏗️ Arxitektura

```
┌─────────────┐      ┌───────────────────────────┐      ┌──────────────┐
│   Client    │ ◄──► │   FastAPI (Port 8000)     │ ◄──► │  ChromaDB    │
└─────────────┘      └─────────────┬─────────────┘      └──────────────┘
                                   │
                     ┌─────────────▼─────────────┐      ┌──────────────┐
                     │   RAG Workflow            │ ◄──► │ Google AI    │
                     │ 1. Vector Search          │      │ Gemini Model │
                     │ 2. Prompt Engineering     │      └──────────────┘
                     │ 3. LLM Generation         │
                     └───────────────────────────┘
```

**Texnologiyalar:**
- **Backend:** FastAPI
- **Vektor DB:** ChromaDB
- **LLM:** Google Gemini 2.5 Flash Lite
- **Embeddings:** HuggingFace `all-MiniLM-L6-v2`
- **Orchestration:** LangChain

---

## 🚀 Tezkor boshlash

### Shartlar
- Python 3.12+
- Google AI Studio API Key

### 1. Sozlash

```bash
git clone <repository-url>
cd PostgreAI
cp .env_example .env  # GOOGLE_API_KEY ni kiriting
```

### 2. Kutubxonalarni o'rnatish

```bash
pip install -r requirements.txt
```

### 3. Ma'lumotlarni bazaga yuklash (Ingestion)
47 ta JSON faylni vektor ko'rinishiga o'tkazish uchun:

```bash
python ingest.py
```

### 4. Serverni ishga tushirish

```bash
python main.py
```

### 5. Serverga kirish
http://127.0.0.1:8000/docs
---

## 📚 API Hujjatlar

### Asosiy Endpointlar

#### 1. Savol berish (AI Agent)
`POST /answer`

**So'rov:**
```json
{
  "question": "PostgreSQL-da qanday qilib jadval yaratiladi?"
}
```

**Javob:**
```json
{
  "answer": "PostgreSQL-da jadval yaratish uchun CREATE TABLE buyrug'idan foydalaniladi..."
}
```



## 🛠️ Loyiha strukturasi

```text
PostgreAI/
├── src/
│   ├── api/          # FastAPI routerlari
│   ├── ingestion/    # JSON loader (Generator-based)
│   ├── chunking/     # Text splitters
│   ├── llm/          # Gemini AI client
│   ├── retrieval/    # Vector search logic
│   └── vectordb/     # ChromaDB configuration
├── data/             # 47 ta PostgreSQL JSON fayllari
├── vector_db/        # Saqlangan vektorlar (Persist)
├── ingest.py         # Data pipeline skripti
├── main.py           # API va Web Server
├── Dockerfile        # Containerization
└── requirements.txt  # Bog'liqliklar
```

---

## 📊 Ma'lumotlar formati

Hujjatlar quyidagi JSON formatida saqlanadi:
```json
[
  {
    "title": "Mavzu nomi",
    "url": "https://postgresql.org/docs/...",
    "content": "To'liq texnik matn..."
  }
]
```

---

## 🐳 Docker

Loyihani Docker orqali ishga tushirish:

```bash
docker build -t postgre-ai .
docker run -p 8000:8000 --env-file .env -v $(pwd)/vector_db:/app/vector_db postgre-ai
```

---

## 📝 Litsenziya

MIT litsenziyasi ostida tarqatiladi. Batafsil [LICENSE](LICENSE) faylida.

---

**PostgreSQL hujjatlari uchun yaratildi.**