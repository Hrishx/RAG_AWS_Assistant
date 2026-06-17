# AWS Agreement RAG Assistant 🤖

A Retrieval-Augmented Generation (RAG) based Question Answering system built on the AWS Customer Agreement document.

The system allows users to ask questions about the AWS Agreement PDF and returns AI-generated answers with supporting source snippets.

It also tracks user queries using SQL logging and provides an analytics dashboard.

---

# Architecture Overview

```
AWS Customer Agreement PDF
            |
            v
      PDF Loader
            |
            v
     Text Chunking
            |
            v
   Embedding Generation
            |
            v
      FAISS Vector DB
            |
            v
        Retriever
            |
            v
 Retrieved Context + User Query
            |
            v
        LLM (Ollama)
            |
            v
       FastAPI Backend
            |
            v
 Streamlit Frontend + Analytics
```

---

# Tech Stack

### Backend
- Python
- FastAPI
- LangChain
- FAISS Vector Store
- Ollama LLM
- SQLite Database
- Pydantic

### Frontend
- Streamlit
- Requests

---

# Features

## RAG Pipeline

- Loads AWS Customer Agreement PDF
- Splits document into meaningful chunks
- Converts chunks into embeddings
- Stores embeddings in FAISS
- Retrieves relevant chunks based on user questions
- Generates answers using LLM
- Returns source references

---

## SQL Logging & Analytics

Every question asked by the user is logged.

Stored details:

- User question
- Response latency
- Success / Failure status

Analytics dashboard provides:

- Total number of questions
- Average response latency
- Failed / out-of-context questions

---

# API Endpoints


## Ingest Document

POST

```
/ingest
```

Processes PDF and creates vector embeddings.


---

## Ask Question

POST

```
/ask
```

Example request:

```json
{
 "question":"What are AWS responsibilities?"
}
```

Response:

```json
{
 "answer":"AWS responsibilities include...",
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

- total queries
- average latency
- failed questions


---

# Design Decisions


## Chunking Strategy

Chunk Size: 1000 characters

Chunk Overlap: 200 characters


Reason:

Large enough to preserve context from legal documents while overlap prevents information loss between chunks.


---

## Retriever

Top-K: 3

Reason:

Retrieving top 3 chunks provides enough relevant context without increasing unnecessary LLM tokens.


---

## Model Choice

LLM:

Ollama local model

Reason:

- Free inference
- Runs locally
- No external API dependency


Embedding Model:

Sentence Transformer / Ollama Embeddings

Used to convert document chunks into vector representations.


---

# Setup Instructions


## Clone Repository

```bash
git clone <your github link>

cd RAG_AWS_Assistant
```


---

## Create Environment


```bash
conda create -n rag_env python=3.10

conda activate rag_env
```


---

## Install Dependencies


```bash
pip install -r requirements.txt
```


---

# Running Application


## Start Backend


```bash
uvicorn backend.app:app --reload
```


Backend runs at:

```
http://127.0.0.1:8000
```


---

## Start Frontend


Open another terminal:

```bash
streamlit run frontend/app.py
```


Frontend runs at:

```
http://localhost:8501
```


---

# Demo Flow

1. Start FastAPI backend
2. Start Streamlit frontend
3. Ask AWS Agreement related questions
4. View generated answer with source
5. Open analytics dashboard


---

# Project Structure


```
RAG_AWS_Assistant

│
├── backend
│   ├── app.py
│   ├── rag.py
│   ├── database.py
│   ├── schema.py
│
├── frontend
│   └── app.py
│
├── data
│   └── AWS Customer Agreement.pdf
│
├── requirements.txt
│
└── README.md
```

---

# Author

Harish C

AI / Generative AI Developer