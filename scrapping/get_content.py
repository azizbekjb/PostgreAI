import os
import json

import requests
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import  datetime

from pprint import pprint
BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = str(BASE_DIR).replace("scrapping", "docs/")
def get_content():
    # Sanagichni yuklab olish
    with open(BASE_DIR / 'counter.json', 'r') as file:
        counter = json.load(file)
        part = counter["part"]
        counter = counter["counter"]

    # Linklarni fayllardan yuklab olish
    with open(BASE_DIR / 'all_links.json') as file:
        all_links = json.load(file)

    # Har bir link ichidan matnlarni yuklab olish
    contents = []

    for i in range(counter, len(all_links)):
        item = all_links[i]
        response = requests.get(item["url"])
        soup = BeautifulSoup(response.content, 'html.parser')
        page_contents = soup.find_all("div", class_="sect1")
        try:
            page_text = page_contents[0].text
            new_text = ""
            for text in page_text.split("\n"):
                if len(text) > 0:
                    new_text += "\n" + text

            item["content"] = new_text
            contents.append(item)
            print(f"{i + 1}-sahifadan matnlar olindi |{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}|")

            if len(contents)  == 10 or i == len(all_links) - 1:

                # Har 10 ta maqolada faylni yozish
                part += 1
                filename = DOCS_DIR + f"contents_{part}.json"
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(json.dumps(contents, indent=4))
                    text_to_print = f"|{part}-faylga 10 ta sahifaning matni yuklandi: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}|"
                    print("-"*len(text_to_print))
                    print(text_to_print)
                    print("-" * len(text_to_print))
                contents = []

            # Sanagichni yangilash
            with open(BASE_DIR / 'counter.json', 'w', encoding="utf-8") as file:
                file.write(json.dumps({"counter": i, "part": part}, indent=4, ensure_ascii=False))

        except IndexError:
            print(f"{i+1}-sahifaga kirishda kontent yo'q. URL: {item['url']}")
            pass

if __name__ == "__main__":

    print(f"Web sahifalardan matnlarni olish boshlanmoqda |{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}|")
    print("="*100)
    get_content()
    print(f"Web sahifalardan matnlarni olish yakunlandi |{datetime.now()}|")
    print("=" * 100)