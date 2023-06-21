import requests
from bs4 import BeautifulSoup
import pandas as pd

apt_name = []
apt_desc = []
apt_price = []
apt_reviews = []

#! this url is dynamic. there is an issue for that,in every response it is generating new data,so this code is prohebitate to this kind of websites.
url = 'https://www.airbnb.com/s/New-Delhi--India/homes?property_type_id%5B%5D=1&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab&query=New%20Delhi%2C%20India&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-07-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&ne_lat=28.765938767205803&ne_lng=77.58735284306647&sw_lat=28.08527325989742&sw_lng=77.02408035848828&zoom=10&zoom_level=10&search_by_map=true&search_type=user_map_move'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

# Todo: Here we will extract the links of the rest pages, which urls are not matched with each other
for i in range(1, 5):
    next_page = soup.find('a', class_='l1ovpqvx c1ytbx3a dir dir-ltr')
    if next_page:
        next_page = next_page.get('href')
    else:
        break
    host_page = "https://www.airbnb.com"+next_page
    # print(host_page)
    url = host_page
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    # ? url and data extraction done . data is in html formate right now.
    # Todo: extracting the data in string and understandable formate(below).

    names = soup.find_all('div', class_="t1jojoys dir dir-ltr")
    for i in names:
        name = i.text
        apt_name.append(name)
    # print(len(name))

    prices = soup.find_all('span', class_='a8jt5op dir dir-ltr')
    for i in prices:
        price = i.text
        apt_price.append(price)
    print(len(apt_price))

    descriptions = soup.find_all('div', class_='fb4nyux s1cjsi4j dir dir-ltr')
    for i in descriptions:
        desc = i.text
        apt_desc.append(desc)
    # print(len(apt_desc))

    reviews = soup.find_all('span', class_='r1dxllyb dir dir-ltr')
    for i in reviews:
        review = i.text
        apt_reviews.append(review)
    # print(len(apt_reviews))

# df = pd.DataFrame({"Apartment name": apt_name, "Cost per night": apt_price,
#                    "Apartment description": apt_desc, "Reviews": apt_reviews})

df = pd.DataFrame({"Apartment name": apt_name, "Cost per night": apt_price})
# still not working

print(df)
df.to_csv("name.csv")
