
import requests
from bs4 import BeautifulSoup
import csv

# URL страницы для парсинга
url = "https://4lapy.ru/catalog/sobaki/korm-sobaki/sukhoy-korm-sobaki/"

# Отправка GET-запроса и получение содержимого страницы
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Создание CSV-файла и запись заголовков столбцов
csv_file = open("dog_food.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["ID товара", "Наименование", "Ссылка", "Регулярная цена", "Промо цена", "Бренд"])

# Парсинг данных и запись их в CSV-файл
products = soup.find_all("div", class_="product-item")
for product in products:
    product_id = product.get("data-id")
    name = product.find("div", class_="product-item__title").text.strip()
    link = product.find("a", class_="product-item__img").get("href")
    regular_price = product.find("div", class_="price-block__regular").text.strip()
    promo_price = product.find("div", class_="price-block__special").text.strip()
    brand = product.find("div", class_="product-item__brand").text.strip()

    csv_writer.writerow([product_id, name, link, regular_price, promo_price, brand])

# Закрытие CSV-файла
csv_file.close()

print("Данные успешно сохранены в файл dog_food.csv.")
