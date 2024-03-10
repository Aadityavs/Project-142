from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
page = requests.get(START_URL)
print(page)

browser.get(START_URL)
time.sleep(10)
stars_data = []

soup = BeautifulSoup(browser.page_source, "html.parser")
table = soup.find('table')

temp_list = []
tablerows = table.find_all("tr")

for tr in tablerows:

            td_tags = tr.find_all("td")
            row = [i.text.rstrip() for i in td_tags]
            temp_list.append(row)

star_name = []
radius = []
mass = []
distance = []

for i in range(1,len(temp_list)):
    star_name.append(i[1])
    radius.append(i[9])
    mass.append(i[8])
    distance.append(i[6])

df = pd.DataFrame(list(zip(star_name,radius,mass,distance)),columns = ['Brown dwarf','Distance','Mass','Radius'])
print(df)
df.to_csv('Dwarf_star_info.csv',index=True,index_label='label')