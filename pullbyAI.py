import openpyxl
from bs4 import BeautifulSoup

# Read the HTML file
with open('daraz.html', 'r', encoding='utf8') as file:
    html = file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all divs with class="inner--SODWy"
divs = soup.find_all('div', class_='inner--SODWy')

# Initialize variables
product_name = ''
current_price = ''
previous_price = ''
discount = ''
reviews = ''

# Extract information from each div
for div in divs:
    # Find div with class="title--wFj93"
    title_div = div.find('div', class_='title--wFj93')
    if title_div:
        product_name = title_div.text.strip()

    # Find span with class="currency--GVKjl"
    current_price_span = div.find('span', class_='currency--GVKjl')
    if current_price_span:
        current_price = current_price_span.text.strip()

    # Find del with class="currency--GVKjl"
    previous_price_del = div.find('del', class_='currency--GVKjl')
    if previous_price_del:
        previous_price = previous_price_del.text.strip()

    # Find span with class="discount--HADrg"
    discount_span = div.find('span', class_='discount--HADrg')
    if discount_span:
        discount = discount_span.text.strip()

    # Find span with class="rating__review--ygkUy"
    reviews_span = div.find('span', class_='rating__review--ygkUy')
    if reviews_span:
        reviews = reviews_span.text.strip()

    # Write the extracted data to Excel
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.append(['Product Name', 'Current Price',
                     'Previous Price', 'Discount', 'Reviews'])
    worksheet.append([product_name, current_price,
                     previous_price, discount, reviews])
    workbook.save('product_info.xlsx')
