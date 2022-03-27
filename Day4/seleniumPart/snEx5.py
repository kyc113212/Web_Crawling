from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


searchStr = input("찾을 이미지 이름 : ")
# q=는 쿼리를 나타내고 그 뒤에 찾을 항목을 utf-8항목으로 변환해서(quote_plus) url을 구성한다
baseurl = 'https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q='
#quote_plus메서드로 문자를 utf-8형식으로 변경
url = baseurl+quote_plus(searchStr)
# print(url)

s = Service('../../Day5/webcrawlingPart/chromedriver.exe')
driver = webdriver.Chrome(service=s)
# 창 출력
driver.get(url)
time.sleep(5)

# driver의 page_source를 이용해서 html파일을 받아온다
html = driver.page_source
bsObj = BeautifulSoup(html,'html.parser')

thumnails = bsObj.select('imgList > div > a > img')

import dload

for thumnail in thumnails:
    src = thumnail['src']
    # 파일명의 이름의 숫자를 랜덤하게 주는것
    rvar = str(round(random.random()*1000000))
    # 소스파일을 저장하기 위해 사용, 다운받아올 경로와, 실제 directory에 어떠한 이름으로 저장할지 지정
    #dload.save(src, f'imgs/{searchStr}{rvar}.jpg')

#끝나면 창을 꺼준다다
driver.quit()

#다운로드를 위해서는 pip install dload를 설치해야한다.