from sqlalchemy import create_engine, Column, Integer,String,Float,DateTime
from sqlalchemy.orm import declarative_base,sessionmaker
from datetime import datetime

database_url="sqlite:///logs.db"

engine= create_engine(database_url,connect_args={"check_same_thread":False})

SessionLocal= sessionmaker(bind=engine)

Base= declarative_base()

class query_log(Base):
    __tablename__='query_logs'
    
    id= Column(Integer,primary_key=True,index=True)
    
    question=Column(String)
    
    answer=Column(String)
    
    response_time= Column(Float)
    
    timestamp=Column(DateTime,default=datetime.now)
    
    status=Column(String)

Base.metadata.create_all(engine)

def save_log(question,answer,response_time,status):
    db=SessionLocal()
    log=query_log(question=question,answer=answer,response_time=response_time,status=status)
    db.add(log)
    db.commit()
    db.close()

def get_analytics():
    db=SessionLocal()
    logs=db.query(query_log).all()
    
    total=len(logs)
    
    if total>0:
        avg=sum(log.response_time for log in logs)/total
    else:
        avg=0
    
    failed=[log.question for log in logs if log.status=="failed"]
    
    common={}
    
    for log in logs:
        
        common[log.question]=(common.get(
            log.question,0)+1)
    
    db.close()
    
    return {
        "total_questions":total,

        "average_latency":avg,

        "failed_questions":failed,

        "common_questions":common

    }