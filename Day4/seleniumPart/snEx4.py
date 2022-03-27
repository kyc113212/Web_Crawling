from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

s = Service('../../Day5/webcrawlingPart/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.naver.com')

input_element = driver.find_element(By.NAME, 'query')
input_element.send_keys("python")
# 여기서 엔터키가 Return이다
input_element.send_keys(Keys.RETURN)

from bs4 import BeautifulSoup

# ul - li - a태그순으로 되어있을 때(어떤 태그가 순서대로 있을때) select함수를 이용해서 앞 순서가 포함되는것을 모두 가져온다.
html = driver.page_source
bsObj = BeautifulSoup(html,'html.parser')
tag = bsObj.select('ul > li > a')
for i in tag:
    print(i)