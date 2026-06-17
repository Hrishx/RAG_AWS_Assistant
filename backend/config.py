import os

base_dir=os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

pdf_path=os.path.join(base_dir,"data",'AWS Customer Agreement.pdf')

vector_path=os.path.join(base_dir,'vector_store')

embedding_model=("nomic-embed-text:latest")
llm_model="qwen2.5:3b-instruct"