import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.iplt20.com/auction'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

table = soup.find('table', class_='ih-td-tab auction-tbl', id='t4')
# print(table)
header = table.find_all('th')
# print(header)
header_list = []
for i in header:
    mk_list = i.text
    header_list.append(mk_list)

print(header_list)
df = pd.DataFrame(columns=header_list)
print(df)
rows = table.find_all('tr')
for i in rows[1:]:
    data = i.find_all('td')
    row = [tr.text.strip() for tr in data]
    # print(row)
    l = len(df)
    df.loc[l] = row
df.to_csv('IPL2023_auction_top_byu.csv')
