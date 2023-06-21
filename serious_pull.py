import requests
from bs4 import BeautifulSoup
import pandas as pd

product_name = []
product_price = []
product_desc = []
product_review = []

for i in range(1, 11):
    url = f'https://www.flipkart.com/search?q=mobile+under+20000rs&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+under+20000rs%7CMobiles&requestId=baf917c2-1569-4d14-81ba-1a6637111401&as-searchtext=mobi%3Be+under&page={i}'

    r = requests.get(url)
    print(r)
    # title
    soup = BeautifulSoup(r.text, 'lxml')
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_="_4rR01T")
    for i in names:
        pn = i.text
        product_name.append(pn)
    # print(product_name)
    # price
    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in prices:
        pp = i.text
        product_price.append(pp)
    # print(product_price)
    # description
    descriptions = box.find_all("ul", class_="_1xgFaf")
    for i in descriptions:
        p_d = i.text
        product_desc.append(p_d)
    # print(product_desc)
    # reviews
    reviews = box.find_all("div", class_="_3LWZlK")
    for i in reviews:
        pr = i .text
        product_review.append(pr)
    print(len(product_review))

df = pd.DataFrame({"product name": product_name, "product price": product_price,
                   "product description": product_desc, "product reviews": product_review})
print(df)
df.to_csv('product.csv')


# Todo: we will use a while loop here instead of that for loop avobe . But the case have to be different.When The links will not change according to the i and using a different link in every page.
# ? next_link = box.find('a', class_='_1LKTO3').get("href")
# ?complete_nxt_link = "https://www.flipkart.com"+next_link
# ? print(complete_nxt_link)
# ? url = complete_nxt_link
# ? r = requests.get(url)
# ?soup = BeautifulSoup(r.text, 'lxml')
