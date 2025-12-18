# Ковалёв Стас Вариант 4
import requests
from bs4 import BeautifulSoup
import json

def parse_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")
    quotes_data = []

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        quotes_data.append({"quote": text, "author": author})

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(quotes_data, f, ensure_ascii=False, indent=4)

    print("Данные успешно сохранены в файл data.json")

if __name__ == "__main__":
    parse_quotes()