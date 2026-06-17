from src.ingestion.loader import load_json_files
from src.chunking.chunker import split_documents
from src.vectordb.vector_store import store

from dotenv import load_dotenv
import warnings

warnings.filterwarnings("ignore")
load_dotenv()

def main():
    # 1. Hujjatlarni yuklash
    raw_docs = load_json_files("data/")
    
    # 2. Hujjatlarni bo'laklash
    final_chunks = split_documents(raw_docs)
    
    # 3. Vektor DB ga saqlash
    store(all_splits=final_chunks)
if __name__ == "__main__":
    main()