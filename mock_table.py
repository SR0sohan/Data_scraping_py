import requests
import pandas as pd
from bs4 import BeautifulSoup

link = 'https://webscraper.io/test-sites/tables/tables-semantically-correct'

r = requests.get(link)
# print(r)

soup = BeautifulSoup(r.text, 'lxml')
table = soup.find('table', class_='table table-bordered')
# print(table)
header = table.find_all('th')
header_list = []
for i in header:
    h_list = i.text
    header_list.append(h_list)
print(header_list)

df = pd.DataFrame(columns=header_list)

rows = table.find_all('tr')
for i in rows[1:]:
    data = i.find_all('td')
    row = [i.text.strip() for i in data]
    # print(row)
    l = len(df)
    df.loc[l] = row
# print(df)
df.to_csv('mock.csv')
