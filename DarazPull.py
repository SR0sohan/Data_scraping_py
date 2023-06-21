import pandas as pd
from bs4 import BeautifulSoup
import requests


data = {"product name": [], "Actual price": [], "Discout percent": [],
        "Discount price": [], "Reviews": [], "Location": []}


#! this one does not work in a javascript driven web page but any other page is good.
for i in range(1, 11):
    url = (
        f'https://www.daraz.com.bd/catalog/?_keyori=ss&from=input&page={i}&q=shirt%20for%20men%20under%20300&spm=a2a0e.searchlist.search.go.6d755a45WPWHil')
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    boxes = soup.find_all("div", class_='inner--SODwy')
    print(boxes)

    for box in boxes:
        name = box.find("div", class_="title--wFj93")
        print(name)
        if name:
            data["product name"].append(name.text)
        else:
            data["product name"].append('')

        actual_price = box.find("del", class_="currency--GVKjl")
        if actual_price:
            data["Actual price"].append(actual_price.text)
        else:
            data["Actual price"].append('')

        discount_percent = box.find('span', class_='discount--HADrg')
        if discount_percent:
            data["Discout percent"].append(discount_percent.text)
        else:
            data["Discout percent"].append('')

        discount_price = box.find('span', class_="currency--GVKjl")
        if discount_price:
            data["Discount price"].append(discount_price.text)
        else:
            data["Discount price"].append('')

        reviews = box.find('span', class_="rating__review--ygkUy")
        if reviews:
            data["Reviews"].append(reviews.text)
        else:
            data["Reviews"].append('')

        location = box.find('span', class_="location--eh0Ro ")
        if location:
            data["Location"].append(location.text)
        else:
            data["location"].append('')

df = pd.DataFrame(data)
print(df)
# df.to_csv('test_around.csv')
