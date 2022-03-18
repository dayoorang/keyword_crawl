from bs4 import BeautifulSoup
from lxml import etree
import requests
import urllib.request
from urllib.parse import urlparse, urlencode
import numpy as np
import re

from tqdm import tqdm
from konlpy.tag import Kkma
from collections import Counter
import os 
from dotenv import load_dotenv

load_dotenv()
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-17.0.2\bin\server'


kkma = Kkma() 
url = os.environ.get("url")


headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            }

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')




lines = []
h1_tag = soup.find_all('h1')
h1_list = [ h1.get_text().strip() for h1 in h1_tag ]
# print('h1_list :', h1_list)
lines.extend(h1_list)


h2_tag = soup.find_all('h2')
h2_list = [ h2.get_text().strip() for h2 in h2_tag ]
# print('h2_list :', h2_list)
lines.extend(h2_list)


h3_tag = soup.find_all('h3')
h3_list = [ h3.get_text().strip() for h3 in h3_tag ]
# print('h3_list :', h3_list)
lines.extend(h3_list)


h4_tag = soup.find_all('h4')
h4_list = [ h4.get_text().strip() for h4 in h4_tag ]
# print('h4_list :', h4_list)
lines.extend(h4_list)


p_tag = soup.find_all('p')
p_list = [ p.get_text().strip() for p in p_tag if p.get_text().strip() != '']
# print('p_list :', p_list)
lines.extend(p_list)

# print('lines : \n', lines)
# print('갯수 :',len(lines))

tokens = []

for line in tqdm(lines):
  tokenized = kkma.nouns(line)
  for token in tokenized:
    tokens.append(token)

counts = Counter(tokens)
print(counts.most_common(30))