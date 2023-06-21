import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

apt_name = []
apt_desc = []
apt_price = []
apt_reviews = []

#! this is a refactored code of unmatched_href.py.hence the data are still not collectable for the websites dynamic behaviour!

url = 'https://www.airbnb.com/s/New-Delhi--India/homes?property_type_id%5B%5D=1&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab&query=New%20Delhi%2C%20India&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-07-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&ne_lat=28.765938767205803&ne_lng=77.58735284306647&sw_lat=28.08527325989742&sw_lng=77.02408035848828&zoom=10&zoom_level=10&search_by_map=true&search_type=user_map_move'

while True:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    # Data extraction from HTML
    names = soup.find_all('div', class_="t1jojoys dir dir-ltr")
    descriptions = soup.find_all('div', class_='fb4nyux s1cjsi4j dir dir-ltr')
    prices = soup.find_all('span', class_='_tyxjp1')
    reviews = soup.find_all('span', class_='r1dxllyb dir dir-ltr')

    # Check if all arrays have the same length
    if len(names) != len(descriptions) or len(names) != len(prices) or len(names) != len(reviews):
        break

    # Append data to arrays
    for name in names:
        apt_name.append(name.text)

    for desc in descriptions:
        apt_desc.append(desc.text)

    for price in prices:
        apt_price.append(price.text)

    for review in reviews:
        apt_reviews.append(review.text)

    # Find next page link
    next_page = soup.find('a', class_='l1ovpqvx c1ytbx3a dir dir-ltr')
    if not next_page:
        break

    url = "https://www.airbnb.com" + next_page.get('href')
    # Add a delay between requests to be more respectful to the website
    time.sleep(1)

# Create DataFrame
df = pd.DataFrame({"Apartment name": apt_name, "Cost per night": apt_price,
                  "Apartment description": apt_desc, "Reviews": apt_reviews})

print(df)
df.to_csv("recon.csv")
