import requests
from bs4 import BeautifulSoup
import pandas as pd

link = 'https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets'

val = requests.get(link)
soup = BeautifulSoup(val.text, "lxml")


title = soup.find_all("a", class_="title")
product_name = []
for i in title:
    name = i.text
    product_name.append(name)

# print(product_name)

prices = soup.find_all("h4", class_="pull-right price")
price_list = []
for i in prices:
    price = i.text
    price_list.append(price)

# print(price_list)

desc = soup.find_all("p", class_="description")
desc_list = []
for i in desc:
    description = i.text
    desc_list.append(description)

# print(desc_list)

reviews = soup.find_all("p", class_="pull-right")
review_list = []
for i in reviews:
    review = i.text
    review_list.append(review)

# print(review_list)

df = pd.DataFrame(
    {"Product Name": product_name, "price": price_list, "Product Detail": desc_list, "Product Reviews": review_list})

# print(df)
df.to_csv("Product Detail.csv")
# df.to_excel('product.xlsx')
