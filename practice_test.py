import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://webscraper.io/test-sites/tables'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
# print(soup)
table = soup.find('table', class_='table table-bordered')
headers = table.find_all('th')
# print(headers)
titles = []
for i in headers:
    title = i.text
    titles.append(title)
# print(titles)
df = pd.DataFrame(columns=titles)
rows = table.find_all('tr')
for i in rows[1:]:
    datas = i.find_all('td')
    row = [tr.text for tr in datas]
    print(row)
    length = len(df)
    df.loc[length] = row
print(df)
df.to_csv('sample.csv')
