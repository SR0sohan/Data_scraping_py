import pandas as pd
from bs4 import BeautifulSoup
import requests

data = {"product name": [], "Description": [], "price": [], "Reviews": []}

for i in range(2, 8):
    url = 'https://www.flipkart.com/search?q=mobile+under+55000rs&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&augment=false&page=' + \
        str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    rows = soup.find_all('div', class_="_2kHMtA")

    for row in rows:
        name = row.find('div', class_="_4rR01T")
        if name:
            data["product name"].append(name.text)
        else:
            data["product name"].append('')

        desc = row.find('ul', class_="_1xgFaf")
        if desc:
            data["Description"].append(desc.text)
        else:
            data["Description"].append('')

        price = row.find('div', class_="_30jeq3 _1_WHN1")
        if price:
            data["price"].append(price.text)
        else:
            data["price"].append('')

        review = row.find('div', class_="_3LWZlK")
        if review:
            data["Reviews"].append(review.text)
        else:
            data["Reviews"].append('')

df = pd.DataFrame(data)
df.to_csv('testone.csv')
