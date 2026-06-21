from src.ingestion.loader import load_json_files
from src.chunking.chunker import split_documents
from src.vectordb.vector_store import store

from dotenv import load_dotenv
from datetime import datetime
import warnings

warnings.filterwarnings("ignore")
load_dotenv()

def main():
    # 1. Hujjatlarni yuklash
    print(f"1. Hujjatlarni yuklash boshlanmoqda... | {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}")
    print("="*80)
    raw_docs = load_json_files("data/")
    print(f"1. Hujjatlarni yuklash tugadi. | {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}")
    print("="*80)

    # 2. Hujjatlarni bo'laklash
    print(f"2. Hujjatlarni bo'laklarga ajratilmoqda... | {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}")
    print("="*80)
    final_chunks = split_documents(raw_docs)
    print(f"2. Hujjatlarni bo'laklarga ajratildi | {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}")
    print("="*80)

    # 3. Vektor DB ga saqlash
    print(f"3. Bo'laklar vektorli ma'lumotlar bazasiga saqlanmoqda... | {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}")
    print("="*80)
    store(all_splits=final_chunks)
    print(f"3. Bo'laklar vektorli ma'lumotlar bazasiga saqlandi. | {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}")
    print("="*80)
if __name__ == "__main__":
    main()