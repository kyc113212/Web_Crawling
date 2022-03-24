# selenium은 자바스크립트를 이용하는 것(getElementbyID와 같은 형식을 사용할 수 있다)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')

from selenium.webdriver.common.by import By
import time

# 최신버전은 find_element에서 참고할 객체와 뒤에 객체의 명칭을 전달하는 것이다
# 아래와 같이 하면 너무 빠르게 화면전환이 되기 때문에 보안관련이 잘되어 있는 웹사이트는 검증이 들어간다.
time.sleep(1)
driver.find_element(By.ID, 'id').send_keys('')
driver.find_element(By.ID, 'pw').send_keys('')
#버튼에 대한 객체는 클릭 method로 사용할 수 있다.
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()