from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('../webcrawlingPart/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://danawa.com/')
time.sleep(3)


# 마우스 커서를 이동하기 위해사용
from selenium.webdriver.common.action_chains import ActionChains

def mouseOverElement(title):
    # 텍스트의 내용을 통해서 내용을 가져오겠다
    element = driver.find_element(By.LINK_TEXT, title)
    #인스턴스가 어떤 드라이서에서 움직이는지 먼저 설정해주어야 한다.
    ActionChains(driver).move_to_element(element).perform()
    return element

# 먼저 제일 처음 시작하는 가전·TV를 소스코드로 text명을 읽어오고 하위는 text를 보고 읽어온다
# 가전티비, 티비까지는 커서를 옮기는 것만 진행하고 이후 전체상품에서 click을 할수 있도록 구현
mouseOverElement('가전·TV')
mouseOverElement('TV')
mouseOverElement('TV 전체 상품').click()
