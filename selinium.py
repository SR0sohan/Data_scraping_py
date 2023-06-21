from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# import time


s = Service('C:/Terminal-X/selinium/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.tutorialsfreak.com/')
# time.sleep(2)

height = driver.execute_script('return document.body.scrollHeight')
print(height)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

# driver.find_element("xpath", "/html/body/div/div/div/section[1]/div/div[1]/div/div/div").screenshot(
#     "C:/Z__Excalibur/Simply_programming/python T/BeautifulSoup/sgagsss.png")

# driver.save_screenshot(
#     'C:/Z__Excalibur/Simply_programming/python T/BeautifulSoup/sceersss.png')

# logers = driver.find_element(
#     "xpath", "/html/body/section[1]/div/div/div[1]/div/div/a").click()
