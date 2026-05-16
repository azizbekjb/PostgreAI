import json

import requests
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import  datetime
BASE_DIR = Path(__file__).resolve().parent

def get_current_links():
    """Bu funksiya PostgreSQL dokumentatsiyaning
    https://www.postgresql.org/docs/current/preface.html sahifasidagi barcha url manzillarini yuklab oladi"""

    BASE_URL = "https://www.postgresql.org/docs/current/"

    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    table_of_contents = soup.find_all("dl", class_="toc")
    table_of_contents_html = BeautifulSoup(str(table_of_contents), "html.parser")
    table_of_contents_links = table_of_contents_html.find_all("a")
    links = []
    for data in table_of_contents_links:
        link = data["href"]
        text = data.get_text(strip=False)
        links.append({
            "title": text,
            "url": BASE_URL + link
        })

    with open(BASE_DIR / "current.json", "w") as file:
        json.dump(links, file, indent=4)

def get_all_chapters_links():
    BASE_URL = "https://www.postgresql.org/docs/current/"

    with open(BASE_DIR / "current.json", "r") as file:
        links = json.load(file)

    all_links = []
    for data in links:
        # Har bobga kirish
        url = data["url"]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Sahifadan kerakli qismini ajratib olish
        all_links_html = soup.find_all("dl", class_="toc")
        all_links_on_page_html = BeautifulSoup(str(all_links_html), "html.parser")
        all_links_on_page_links = all_links_on_page_html.find_all("a") # Linklar

        # Linklar va sarlavhalarni ajratib olish
        new_links = []
        for link in all_links_on_page_links:
            url = BASE_URL +  link.get("href")
            title = link.get_text(strip=False)
            data_to_append = {"url": url, "title": title}

            if data_to_append not in all_links and "#" not in url:
                new_links.append(data_to_append)
                all_links.append(data_to_append)
        data["data"] = new_links

    with open(BASE_DIR / "chapters.json", "w") as file:
        json.dump(links, file, indent=4)

    with open(BASE_DIR / "all_links.json", "w") as file:
        json.dump(all_links, file, indent=4)



if __name__ == "__main__":
    print("1. Asosiy sahifadan linklar olinmoqda...")
    print(f"Boshlandi: {datetime.now()}")
    get_current_links()
    print("1. Asosiy safidan linklar olindi.",)
    print(f"Tugadi: {datetime.now()}\n", "="*100 )

    print("2. Har bob ichidan linklar olinmoqda...")
    print(f"Boshlandi: {datetime.now()}")
    get_all_chapters_links()
    print("2. Har bob ichindan linklar olindi.")
    print(f"Tugadi: {datetime.now()}\n", "="*100 )
