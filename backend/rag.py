from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from backend.config import pdf_path, vector_path, embedding_model, llm_model


class rag_pipeline:
    def __init__(self):
        self.embedding= OllamaEmbeddings(model=embedding_model)
        self.llm=ChatOllama(model=llm_model,temperature=0)
    
    def ingest_pdf(self):
        loader=PyPDFLoader(pdf_path)
        documents=loader.load()
        
        splitter= RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        chunks=splitter.split_documents(documents)
        
        vector_db=FAISS.from_documents(chunks,self.embedding)
        
        vector_db.save_local(vector_path)
        
        return {"Message":"PDF Ingested","chunks":len(chunks)}
    
    def get_retriever(self):
        vector_db= FAISS.load_local(vector_path,self.embedding, allow_dangerous_deserialization=True)
        
        retriever=vector_db.as_retriever( search_kwargs={'k':3})
        return retriever
    
    def create_chain(self):
        retriever=self.get_retriever()
        prompt=ChatPromptTemplate.from_template(
            """
            You are an AWS Customer Agreement Assistant.
            Answer only using the given context.
            
            if the answer is not inside the document say:
            "Sorry, I cannot answer from provided document"
            
            Context:
            {context}
            
            Question:
            {question}
            
            Answer:
            """
        )
        
        con={"context":retriever,"question": RunnablePassthrough()}
        chain=(con|prompt|self.llm|StrOutputParser())
        return chain
    
    def ask(self,question):
        retriever=self.get_retriever()
        chain=self.create_chain()
        answer=chain.invoke(question)
        docs=retriever.invoke(question)
        
        sources=[]
        
        for doc in docs:
            sources.append(
                {"page":doc.metadata.get("page"),"content":doc.page_content[:300]}
            )
        if "cannot answer" in answer.lower():

            sources=[]


        return {
            "answer":answer,
            "sources":sources
        }