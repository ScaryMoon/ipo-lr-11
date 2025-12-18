# Ковалёв Стас Вариант 4
import requests
from bs4 import BeautifulSoup

def parse_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for i, quote in enumerate(quotes, 1):
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        print(f"{i}. Quote: {text}; Author: {author};")

if __name__ == "__main__":
    print("Сбор цитат с сайта Quotes to Scrape:")
    parse_quotes()