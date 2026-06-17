from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_chroma import Chroma

# Bitta umumiy nom va model
DB_NAME = "postgresql_collection"
DB_PATH = "vector_db/"
EMBED_MODEL = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def get_vector_store():
    """Bazani har doim bir xil sozlamalar bilan yuklash uchun funksiya"""
    return Chroma(
        collection_name=DB_NAME,
        persist_directory=DB_PATH,
        embedding_function=EMBED_MODEL
    )

def store(all_splits):
    vector_db = get_vector_store()
    document_ids = vector_db.add_documents(documents=all_splits)
    print(f"{len(document_ids)} ta chunk bazaga muvaffaqiyatli saqlandi.")
    return document_ids