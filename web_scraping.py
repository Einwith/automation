from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(executable_path=r"/Users/xb/Downloads/chromedriver")

name = []
dailyChange = []
driver.get('https://money.usnews.com/investing/stocks/advertising-marketing-services')

content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('span', attrs={'class': 'Span-sc-19wk4id-0 hwDsIC'}):
    name.append(str(a.text).strip())

for b in soup.findAll('strong', attrs={'class': 'Strong-sc-1m7huwa-0 dsjguI'}):
    dailyChange.append(str(b.text).strip())




print(name)
print(dailyChange)