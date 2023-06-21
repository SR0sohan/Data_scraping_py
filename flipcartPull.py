import pandas as pd
from bs4 import BeautifulSoup
import requests

# ?the solution is in the errorHandle.txt page

product_name = []
product_desc = []
product_prize = []
product_rating = []

# !this code doesn't work i failed to colve the problem of unmatched datas.those emy reviews from the web page they can not handled with this code formate.the line line iteration is the possible solution for this. i am wokring on it right now.
for i in range(2, 8):
    url = 'https://www.flipkart.com/search?q=mobile+under+55000rs&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&augment=false&page=' + \
        str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    box = soup.find('div', class_="_1YokD2 _3Mn1Gg")  # ! a modification point

    names = box.find_all('div', class_="_4rR01T")
    for i in names:
        nam = i.text
        product_name.append(nam)
    # print(len(product_name))

    descs = box.find_all('ul', class_="_1xgFaf")
    for i in descs:
        des = i.text
        product_desc.append(des)
    # print(len(product_desc))

    prices = box.find_all('div', class_="_30jeq3 _1_WHN1")
    for i in prices:
        price = i.text
        product_prize.append(price)
    # print(len(product_prize))

    reviews = box.find_all('div', class_="_3LWZlK")
    for i in reviews:
        review = i.text
        product_rating.append(review)
    # print(len(product_rating))

df = pd.DataFrame({"pruduct name": product_name, "Description": product_desc,
                  "price": product_prize, "Reviews": product_rating})
df.to_csv('testtwo.csv')
# for i in range(2, 8):
#     url = 'https://www.flipkart.com/search?q=mobile+under+55000rs&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&augment=false&page=' + \
#         str(i)
#     r = requests.get(url)
#     # print(r)
#     soup = BeautifulSoup(r.text, 'lxml')
#     np = soup.find('a', class_='_1LKTO3').get('href')
#     cnp = "https://www.flipkart.com"+np
#     print(cnp)
#! url = cnp
#! r = requests.get(url)
#! soup = BeautifulSoup(r.text, 'lxml')
