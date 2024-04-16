import requests
from bs4 import BeautifulSoup

url = "https://www.bookvoed.ru/books?genre=60"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

books_count_tag = soup.find("span", class_="category__count")

if books_count_tag:
    books_count = books_count_tag.text
    print("Количество предлагаемых книг в категории 'ИнЯз':", books_count)
else:
    print("Количество предлагаемых книг не найдено")
