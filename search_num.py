import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

from keyword_search import selenium_start, search_click, save_csv

 #keyword_list(끈기)

df = pd.read_csv('keyword_list(끈기).csv')

url = "https://whereispost.com/keyword/" 
selenium_start(url)

list_keywords = []
for index, row in keyword_list.iterrows(): 
    keyword = row[0]
    list_keywords['검색수'].append(search_click(keyword))


df['검색수'] = list_keywords
df.to_csv(f"./keyword_list({keyword}).csv", encoding='utf-8-sig', index=False)

print(list_keywords)
