# AWS Agreement RAG Assistant 🤖

A Retrieval-Augmented Generation (RAG) based AI Question Answering Assistant built using the AWS Customer Agreement document.

The system allows users to ask natural language questions about the AWS Agreement PDF and generates context-aware answers using a local Large Language Model (LLM).

It retrieves relevant document sections using semantic search and provides answers with source references.

The application also tracks user queries using SQLite logging and provides an analytics dashboard.

---

# 🎥 Demo Video

A short project demonstration video is included.

Demo covers:

- FastAPI backend execution
- Streamlit user interface
- Document-based question answering
- Source reference display
- Query analytics dashboard

Demo File:

```
AWS RAG Assistant Demo.mp4
```

---

# 📄 Technical Report

Complete project documentation report is included.

The report contains:

- Problem statement
- Architecture explanation
- Technology stack
- RAG pipeline workflow
- Implementation details
- Testing results
- Future improvements

Report File:

```
AWS_RAG_Assistant_Technical_Report.pdf
```

---

# Architecture Overview

```
AWS Customer Agreement PDF
            |
            v
      PyPDFLoader
            |
            v
RecursiveCharacterTextSplitter
            |
            v
       Text Chunks
            |
            v
Ollama Embeddings (nomic-embed-text)
            |
            v
      FAISS Vector Database
            |
            v
        Retriever
            |
            v
 Retrieved Context + User Question
            |
            v
   LCEL RAG Chain + Prompt
            |
            v
 Qwen2.5 LLM (Ollama)
            |
            v
   Generated Answer + Sources
            |
            v
 FastAPI Backend + Streamlit UI
```

---

# Tech Stack

## Backend

- Python
- FastAPI
- LangChain
- LCEL (LangChain Expression Language)
- FAISS Vector Database
- Ollama Embeddings
- Qwen2.5 LLM
- SQLite
- SQLAlchemy
- Pydantic

## Frontend

- Streamlit
- Requests

---

# Features

## RAG Pipeline

- Loads AWS Customer Agreement PDF
- Extracts document content
- Splits text into optimized chunks
- Generates vector embeddings
- Stores embeddings using FAISS
- Performs semantic similarity search
- Retrieves relevant document context
- Generates LLM answers using retrieved context
- Provides source references with page information

---

# Hallucination Control

The assistant is restricted to AWS Agreement content.

Example:

Question:

```
Who won IPL?
```

Response:

```
Sorry, I cannot answer from provided document
```

This prevents unrelated LLM-generated responses.

---

# SQL Logging & Analytics

Every user interaction is stored.

Logged details:

- User question
- Generated answer
- Response latency
- Success / failure status

Analytics dashboard provides:

- Total number of questions
- Average response time
- Failed/out-of-context questions
- Frequently asked questions

---

# API Endpoints

## Ingest Document

POST

```
/ingest
```

Purpose:

Processes PDF, creates embeddings and stores FAISS vector index.

---

## Ask Question

POST

```
/ask
```

Example Request:

```json
{
 "question":"What are AWS responsibilities?"
}
```

Example Response:

```json
{
 "answer":"According to AWS Customer Agreement...",
 "sources":[]
}
```

---

## Analytics

GET

```
/analytics
```

Returns:

- Total queries
- Average latency
- Failed questions
- Common questions

---

# Design Decisions


## Chunking Strategy

Configuration:

```
chunk_size = 1000

chunk_overlap = 200
```

Reason:

Large enough to maintain legal document context while overlap prevents information loss between chunks.

---

# Retriever Strategy

Configuration:

```
Top K = 3
```

Reason:

Retrieves the three most relevant chunks to provide enough context without increasing unnecessary tokens.

---

# Model Selection

## Embedding Model

```
nomic-embed-text
```

Purpose:

Converts text chunks and user queries into numerical vector representations for semantic search.

---

## LLM

```
Qwen2.5:3B-Instruct using Ollama
```

Reason:

- Local inference
- No external API dependency
- Privacy friendly
- Cost efficient

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/Hrishx/RAG_AWS_Assistant

cd RAG_AWS_Assistant
```

---

# Create Environment

```bash
conda create -n rag_env python=3.10

conda activate rag_env
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Application


## Start Backend

Run from project root:

```bash
uvicorn backend.main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Start Frontend

Open another terminal:

```bash
streamlit run frontend/app.py
```

Frontend URL:

```
http://localhost:8501
```

---

# Project Structure

```
RAG_AWS_Assistant/

│
├── backend/
│   ├── main.py
│   ├── rag.py
│   ├── database.py
│   ├── schemas.py
│   └── config.py
│
├── frontend/
│   └── app.py
│
├── data/
│   └── AWS Customer Agreement.pdf
│
├── vector_store/
│   ├── index.faiss
│   └── index.pkl
│
├── AWS_RAG_Assistant_Demo.mp4
│
├── AWS_RAG_Assistant_Technical_Report.pdf
│
├── requirements.txt
│
└── README.md
```

---

# Future Improvements

- Add authentication
- Deploy using Docker
- Add cloud vector database support
- Support multiple document uploads
- Add conversation memory
- Improve retrieval using reranking

---

# Author

**Harish C**

AI / Generative AI Developer