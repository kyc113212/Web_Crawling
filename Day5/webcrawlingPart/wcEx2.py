from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
from urllib.parse import quote_plus

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

keyword = quote_plus('무선청소기')
total_page = 10
prod_data_total = []

def get_prod_items(prod_items):
    prod_data = []
    for prod_item in prod_items:
        try:
            title = prod_item.select('p.prod_name > a')[0].text.strip()
        except:
            title = ''
        try:
            spec_list = prod_item.select('div.spec_list')[0].text.strip()
        except:
            spec_list = ''
        try:
            price = prod_item.select('li.rank_one > p.price_sect > a > strong')[0].text.strip().replace(',','')
        except:
            price = ''
        prod_data.append([title,spec_list,price])
    return prod_data

def get_serach_page_url(keyword, page):
    # 쿼리 파트 {]로 처리, 페이지정보 입력으로 변경, sort, list, booster, addDelivery=N까지는 필요, 탭에 물품보이느 것도 필요
    # string문자에 뒤에 format을 붙여서 {}로 처리한 것에 format에 넣은 변수를 집어넣는다
    return 'http://search.danawa.com/dsearch.php?query={}&originalQuery=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&volumeType=allvs&page={}&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&tab=goods'.format(keyword,page)
# url = 'http://search.danawa.com/dsearch.php?query=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&originalQuery=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&volumeType=allvs&page=2&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=102207&defaultPhysicsCategoryCode=72%7C80%7C81%7C0&defaultVmTab=2887&defaultVaTab=378682&tab=goods'

for page in range(1,total_page+1):
    url = get_serach_page_url(keyword,page)
    driver.get(url)
    time.sleep(4)

    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    prod_items = soup.select('div.main_prodlist > ul.product_list > li.prod_item')
    prod_item_list = get_prod_items(prod_items)
    prod_data_total = prod_data_total + prod_item_list
# print(prod_data_total)

import pandas as pd

data = pd.DataFrame(prod_data_total,
                    columns=['상품명','스펙 목록','가격'])

data.to_csv('./files/danawa_crawling_result.csv',index=False)
driver.quit()