from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pyperclip

import os
from dotenv import load_dotenv

load_dotenv()

uid = os.environ.get("uid")
upw = os.environ.get("upw")


## 모바일 버젼 접속 
# mobile_emulation = { "deviceName": "iPhone X" } 
# chrome_options = webdriver.ChromeOptions() 
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation) 
# driver = webdriver.Chrome(options=chrome_options)

#드라이버 로딩 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#네이버 로그인 주소 
url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com' 
uid = uid 
upw = upw
 #네이버 로그인 페이지로 이동 
driver.get(url)
time.sleep(2)
#로딩 대기 #아이디 입력폼 
tag_id = driver.find_element_by_name('id') 
#패스워드 입력폼 
tag_pw = driver.find_element_by_name('pw')
# id 입력 # 입력폼 클릭 -> paperclip에 선언한 uid 내용 복사 -> 붙여넣기
tag_id.click() 
pyperclip.copy(uid)
tag_id.send_keys(Keys.CONTROL, 'v') 
time.sleep(1) 
 # pw 입력 # 입력폼 클릭 -> paperclip에 선언한 upw 내용 복사 -> 붙여넣기
tag_pw.click() 
pyperclip.copy(upw) 
tag_pw.send_keys(Keys.CONTROL, 'v') 
time.sleep(1) #로그인 버튼 클릭 
login_btn = driver.find_element_by_id('log.login') 
login_btn.click()
time.sleep(2)

