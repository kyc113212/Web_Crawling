# 셀리니움은 웹브라우저를 키고 control할 수 있게 해준다 -> 웹에서 넘어오는 view객체에 접근 및 event객체를 다룰 수 있다(button click)
# 크롬의 버전에 맞춰서 selenium을 확인해야하기 때문에 -도움말-버전에 들어가서 버전 확인이 필요
# 필요는 webbrower driver와 selenium모듈 설치가 필요하다

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('../../Day5/webcrawlingPart/chromedriver.exe')
#서비스에 크롭 드라이버가 올라가있는 객체를 올려준다
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(3)
driver.get('https://www.google.com')