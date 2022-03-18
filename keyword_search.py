from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd
import datetime as dt

from bs4 import BeautifulSoup
from lxml import etree
import requests
import urllib.request
from urllib.parse import urlparse, urlencode
import numpy as np
import re

class KeywordSearch:
    def __init__(self, url, keyword):
        self.url = url 
        self.keyword = keyword
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.keyword_list = {keyword:[]}

    def selenium_start(self):
        #해당 url로 이동 및 최초 검색
        elem = self.driver.get(self.url)


    def search_click(self,key_elem):
        elem = WebDriverWait(self.driver,timeout=5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="keyword"]')))
        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="keyword"]')
        elem.click()
        elem.send_keys(key_elem)
        elem.send_keys(Keys.RETURN)


    def collect_keyword(self):
        elems = self.driver.find_elements(by=By.XPATH, value='//*[@id="relkey"]/li/a')        
        for elem in elems:

            if elem.text not in self.keyword_list[self.keyword]:
                self.keyword_list[self.keyword].append(elem.text)

    def collect_doc_num(self, keyword):
        elem = WebDriverWait(self.driver,timeout=5).until(EC.presence_of_element_located((By.XPATH, f"//a[contains(text(),'{keyword}')]/../../td[5]")))
        num = self.driver.find_element(by=By.XPATH, value=f"//a[contains(text(),'{keyword}')]/../../td[5]").text
        return num 

    def save_csv(self, df=pd.DataFrame([])):
        if df.empty:
            df = pd.DataFrame(self.keyword_list)

        df.to_csv(f"./keyword_list({self.keyword}).csv", encoding='utf-8-sig', index=False)




class KeywordSearchGoogle:
    def __init__(self, url, keyword):
        self.keyword = keyword
        self.keyword_list = {keyword:[]}
        self.key_elem = None
        
    def requests_start(self, key_elem):
        self.key_elem= key_elem
        #해당 url로 이동 및 최초 검색
        data = {'q': key_elem,
                'cp': str(len(key_elem)),
                'client': 'gws-wiz',
                'xssi': 't',
                'hl': 'ko',
                'authuser': '0',
                'psi': 'wG4xYoHqGs_pwQOGtLdw.1647406785738',
                'dpr': '1'}

        params = urlencode(data)

        headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
                }

        response = requests.get(f'https://www.google.com/complete/search?{params}', headers=headers)
        
        if response.status_code != 200:
            print(response.status_code)

        return response.text


    def regular_expression_work(self,results):
        p1 = re.compile(r'''(<b>|\\|\d|\[|\]|,|{|}|[a-zA-Z]+|-|:|'|\)|/|_|\.|\?)''')
        results1 = p1.sub('',results)
        p2 = re.compile(r'</>')
        results2 = p2.sub('',results1)
        p3 = re.compile(r'""')
        results3 = p3.sub(',',results2)
        p4 = re.compile(r',,|"|\n')
        results4 = p4.sub('',results3).strip()

        # print('regular_expression_work :\n',results4.split(','))
        return results4.split(',')


    def collect_keyword(self):
        elems = self.regular_expression_work(self.requests_start(self.key_elem))
        for elem in elems:
            if elem not in self.keyword_list[self.keyword] and elem:
                self.keyword_list[self.keyword].append(elem)
        print('keyword list : \n',len(self.keyword_list[self.keyword]))

    def save_csv(self, df=pd.DataFrame([])):
        if df.empty:
            df = pd.DataFrame(self.keyword_list)
    
        df.to_csv(f"keyword_list({self.keyword}_google).csv", encoding='utf-8-sig', index=False)

