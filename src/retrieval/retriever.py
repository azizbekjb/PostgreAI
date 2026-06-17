from src.vectordb.vector_store import get_vector_store

def get_relevant_documents(query: str, k: int = 3):
    """
    Savolga eng yaqin k ta (masalan 3 ta) chunkni bazadan qidirib topadi.
    """
    vector_db = get_vector_store()
    
    # Bazadan qidirish (Similarity Search)
    docs = vector_db.similarity_search(query, k=k)
    
    context = "\n\n".join([doc.page_content for doc in docs])
    
    return context, docs