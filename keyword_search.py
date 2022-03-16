import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
from keyword_list import keyword_list
import datetime as dt


class KeywordSearch:
    def __init__(self, url, keyword):
        self.url = url 
        self.keyword = keyword
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def selenium_start(self):
        #해당 url로 이동 및 최초 검색
        elem = self.driver.get(self.url)


    def search_click(self,key_elem):
        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="keyword"]')
        elem.click()
        elem.send_keys(key_elem)
        elem.send_keys(Keys.RETURN)


    def collect_keyword(self):
        # elems = driver.find_elements_by_xpath('//*[@id="relkey"]/li/a')
        elems = self.driver.find_elements(by=By.XPATH, value='//*[@id="relkey"]/li/a')        
        for elem in elems:
            if elem.text not in list_keywords[self.keyword]:
                list_keywords[self.keyword].append(elem.text)

    def collect_doc_num(self, keyword):
        num = self.driver.find_element(by=By.XPATH, value=f"//a[contains(text(),'{keyword}')]/../../td[5]").text
        return num 

    def save_csv(self, list_keywords=None, df=pd.DataFrame([])):
        # x = dt.datetime.now()
        # date = x.strftime("%Y%m%d%H%M%S")
        # file_name = self.keyword+date
        if df.empty:
            df = pd.DataFrame(list_keywords)

        df.to_csv(f"./keyword_list({self.keyword}).csv", encoding='utf-8-sig', index=False)


keyword ='끈기'
url = "https://whereispost.com/keyword/" 

keyword_list = keyword_list(keyword)



if __name__ == "__main__":
    keyword_search = KeywordSearch(url, keyword)
    keyword_search.selenium_start()
    keyword_search.search_click(keyword)


    list_keywords = {keyword:[]}
    for key_elem in keyword_list:
        keyword_search.search_click(key_elem)
        time.sleep(3)
        keyword_search.collect_keyword()

    keyword_search.save_csv(list_keywords)

    keyword_search.driver.quit()