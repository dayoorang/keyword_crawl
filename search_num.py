import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

from keyword_search import KeywordSearch

 #keyword_list(끈기)

keyword = '공매도'
df = pd.read_csv(f'keyword_list({keyword}).csv')

url = "https://whereispost.com/keyword/" 





if __name__ == "__main__":
    keyword_search = KeywordSearch(url, keyword=keyword)
    keyword_search.selenium_start()


    list_keywords = []
    for index, row in df.iterrows(): 
        if row[0]:
            keyword = row[0]
            keyword_search.search_click(keyword)
            # keyword number
            keyword_num =  keyword_search.collect_doc_num(keyword)
            list_keywords.append(keyword_num)

    df['검색수'] = list_keywords


    keyword_search.save_csv(df=df)

    keyword_search.driver.quit()