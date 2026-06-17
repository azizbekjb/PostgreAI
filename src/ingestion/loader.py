import json
from pathlib import Path

def load_json_files(data_path: str):
    documents = []
    path = Path(data_path)
    
    # Barcha .json fayllarni qidiramiz
    file_list = sorted(path.glob("*.json")) # <--- MANA SHU YERDA TARTIBLANADI
    
    for file_path in file_list:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
          

            
            for item in data:
                doc_text = item.get("content", "")
                metadata = {
                    "source": file_path.name,
                    "title": item.get("title", "No Title"),
                    "url": item.get("url", 'No URL')
                }

                documents.append({"text": doc_text, "metadata": metadata})

            
    print(f"{len(documents)} ta hujjat yuklandi.")
    return documents