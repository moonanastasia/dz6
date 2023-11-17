import requests
from bs4 import BeautifulSoup
import lxml

user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
header = {"User-Agent": user}
session = requests.Session()

for j in range(1, 7):
    print(f"page = {j}")
    url = f"https://cash-backer.club/shops/"
    response = session.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

        all_products = soup.find_all("div", class_="row col-lg-9 col-md-9 col-12")

        for product in all_products:
            if product.find("div", class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link"):
                title = product.find('div', class_="shop-title")
                price = product.find('div', class_="shop-rate")
                print(price.text, title.text)
                #price = price.text.replase("none")
                with open("brand.txt", "a", encoding="utf-8") as file:
                    file.write(f"{price} {title.text}\n")
