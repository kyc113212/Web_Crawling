# 1. 대상 사이트 jolse.com 사이트(http://www.jolse.com/)를 이용합니다.

# 2.메인페이지에서 상단 메뉴중에 SKINCARE 클릭 -> 다음 페이지의  Moisturizers -> Toners & Mists를 클릭하여 다음 페이지로 이동합니다.

# 3. 이동한 화면에서 화장품들의 이름과 가격 정보를 수집합니다.

# 4. 위의 데이터 수집은 1페이지 부터 5페이지까지 진행합니다.

# 5. 이 때 항목 선택을 위해 사용하는 코드와 출력부 코드 부분을 함수화 합니다.

# 6. 출력 결과는 아래와 같이 합니다.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import quote_plus


s = Service('../webcrawlingPart/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://www.jolse.com/')
time.sleep(1)


skin_care_bnt = driver.find_element(By.CLASS_NAME, 'main-quick-skin')
skin_care_bnt.click()

def mouseOverElement(title):
    element = driver.find_element(By.LINK_TEXT, title)
    ActionChains(driver).move_to_element(element).perform()
    return element
time.sleep(1)
mouseOverElement('Toners & Mists').click()
time.sleep(1)

def get_search_page_url(cur_url, page):
    return cur_url + '?page={}'.format(page)

def get_prod_items(prod_items):
    prod_data = []
    for prod_item in prod_items:
        name = prod_item.select('div.description > strong.name > a')[0].text.split(':')[1].strip(' ')
        price_list = prod_item.select('div.description > ul > li:nth-child(1) > span:nth-child(2)')[0].text
        #print(name + " , " + price_list)
        prod_data.append([name,price_list])
    return prod_data

cur_url = driver.current_url
for i in range(1,6):
    new_url = get_search_page_url(cur_url, i)
    driver.get(new_url)
    time.sleep(1)
    html = driver.page_source
    bsObj = BeautifulSoup(html, 'html.parser')

    prod_infos = bsObj.select('div.xans-element-.xans-product.xans-product-normalpackage > div.xans-element-.xans-product.xans-product-listnormal.ec-base-product > ul > li')
    prod_data = get_prod_items(prod_infos)
    for name, price in prod_data:
        print(name + ' , ' + price)
    # for prod_info in prod_infos:
    #     name = prod_info.select('div.description > strong.name > a')[0].text.split(':')[1].strip(' ')
    #     price_list = prod_info.select('div.description > ul > li:nth-child(1) > span:nth-child(2)')[0].text
    #     print(name + " , " + price_list)
driver.quit()
#hint