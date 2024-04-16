import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_page_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # кортеж url-адреса страницы
        parsed_url = urlparse(url)
        print(f"URL адрес страницы: {parsed_url.geturl()}")
        
        # <h1> 
        h1_tags = soup.find_all('h1')
        h1_texts = [tag.get_text() for tag in h1_tags]
        h1_texts_with_links = [str(tag) for tag in h1_tags]
        
        # Вывод заголовков первого уровня
        print("Заголовки первого уровня (тег <h1>):")
        for text, text_with_link in zip(h1_texts, h1_texts_with_links):
            print(text_with_link)
        
       
        response = requests.get(parsed_url.scheme + "://" + parsed_url.netloc)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # кортеж значений url-адреса новые
            print(f"\nURL адрес главной страницы: {parsed_url.scheme}://{parsed_url.netloc}")
            
            # <h2> 
            h2_tags = soup.find_all('h2')
            h2_texts = [tag.get_text() for tag in h2_tags]
            h2_texts_with_links = [str(tag) for tag in h2_tags]
            
            # Вывод заголовков второго уровня
            print("\nЗаголовки второго уровня (тег <h2>):")
            print(", ".join(h2_texts_with_links))
        
    else:
        print("Ошибка при запросе страницы")

if __name__ == "__main__":
    url = input("Введите полный адрес HTML-страницы: ")
    get_page_data(url)
