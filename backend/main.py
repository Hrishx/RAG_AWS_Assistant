from fastapi import FastAPI
import time
from backend.rag import rag_pipeline
from backend.schemas import question_request
from backend.database import save_log, get_analytics

app=FastAPI(title="AWS RAG Assistant")

rag=rag_pipeline()

@app.post("/ingest")
def ingest():
    result=rag.ingest_pdf()
    return result

@app.post("/ask")
def ask(request:question_request):
    start=time.time()
    result=rag.ask(request.question)
    end=time.time()
    
    response_time=end-start
    
    if "connot answer" in result ['answer'].lower():
        status='failed'
    else:
        status='success'
    
    save_log(request.question,result['answer'],response_time,status)
    
    return {
        "answer": result['answer'],
        "sources":result['sources']
    }

@app.get("/analytics")
def analytics():
    return get_analytics()