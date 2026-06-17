from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def split_documents(documents: list, chunk_size: int = 1000, chunk_overlap: int = 100):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    
    chunks = []
    for doc in documents:
        split_texts = text_splitter.split_text(doc["text"])
        
        for i, text in enumerate(split_texts):
            
            chunks.append(
                Document(
                    page_content=text, 
                    metadata={**doc["metadata"], "chunk_id": i}
                )
            )
            
    print(f"Jami {len(chunks)} ta matn bo'laklari hosil bo'ldi.")
    return chunks