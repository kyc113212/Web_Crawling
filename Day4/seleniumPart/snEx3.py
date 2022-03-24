# selenium은 자바스크립트를 이용하는 것(getElementbyID와 같은 형식을 사용할 수 있다)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.naver.com')
time.sleep(1)

login_btn = driver.find_element(By.CLASS_NAME,'ico_naver')
login_btn.click()
time.sleep(1)

tag_id = driver.find_element(By.NAME,'id')
tag_pw = driver.find_element(By.NAME,'pw')

tag_id.clear()
time.sleep(1)
# 카피하는 방법으로 사람이 입력하는 것처럼 한다
# pip install pyperclip을 설치
import pyperclip
tag_id.click()
pyperclip.copy('아이디입력')
from selenium.webdriver.common.keys import Keys
# shift, Enter와 같이 key를 똑같이 사용하게 해주는 것
# tag_id에 send_key메서드를 이용하여 copy한다
# pip install pyautogui는 마우스를 control할 수있는 것들
tag_id.send_keys(Keys.CONTROL,'v')
time.sleep(1)

tag_pw.click()
pyperclip.copy('비밀번호입력')
tag_pw.send_keys(Keys.CONTROL,'v')
time.sleep(1)

log_btn = driver.find_element(By.ID, 'log.login')
log_btn.click()

from bs4 import BeautifulSoup
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
bsObj = BeautifulSoup(html,'html.parser')
print(bsObj)
