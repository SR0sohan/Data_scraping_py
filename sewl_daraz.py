from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Set up the webdriver, "Location": []
driver = webdriver.Chrome()

data = {"product name": [], "Actual price": [], "Discout percent": [],
        "Discount price": [], "Reviews": []}

for i in range(1, 11):
    url = (
        f'https://www.daraz.com.bd/catalog/?_keyori=ss&from=input&page={i}&q=shirt%20for%20men%20under%20300&spm=a2a0e.searchlist.search.go.6d755a45WPWHil')

    # Load the website
    driver.get(url)

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Get the page source
    html = driver.page_source

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')

    boxes = soup.find_all("div", class_='info--ifj7U')

    for box in boxes:
        name = box.find("div", class_="title--wFj93")
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

        # location = box.find('span', class_="location--eh0Ro ")
        # if location:
        #     data["Location"].append(location.text)
        # else:
        #     data["location"].append('')

# Close the webdriver
driver.close()

df = pd.DataFrame(data)
print(df)
df.to_csv('test_around.csv')
