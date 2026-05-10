import json
import requests
from bs4 import BeautifulSoup


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

    with open("current.json", "w") as file:
        json.dump(links, file, indent=4)

def get_all_chapters_links():
    BASE_URL = "https://www.postgresql.org/docs/current/"

    with open("current.json", "r") as file:
        links = json.load(file)


    for data in links:
        url = data["url"]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        all_links_html = soup.find_all("div", class_="toc")

        d = []
        for link in all_links_html:

            d.append({"title": link.get_text(), "url": BASE_URL + str(link.get("href"))})

        data["data"] = d

    with open("chapters.json", "w") as file:
        json.dump(links, file, indent=4)

if __name__ == "__main__":
    print("1. Asosiy sahifadan linklar olinmoqda...")
    get_current_links()
    print("1. Asosiy safidan linklar olindi.\n", "="*100)

    print("2. Har bob ichindan linklar olinmoqda...")
    get_all_chapters_links()
    print("2. Har bob ichindan linklar olindi.\n", "="*100)