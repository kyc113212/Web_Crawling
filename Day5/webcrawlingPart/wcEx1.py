from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver.exe')
url = 'http://search.danawa.com/dsearch.php?k1=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&module=goods&act=dispMain'
driver.get(url)
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

# 리스트에 있는 아이템을 가지고 올때 parent 아래 1,2,3이 있는 경우 select시 1,2,3의 parent를 불러오는 것이 아니라,
# 1,2,3의 공통된 id값을 가지고와야 prod_items에 리스트로 저장된다
prod_items = soup.select('div.main_prodlist > ul.product_list > li.prod_item')
#print(prod_items[0])

# prod_items[1] 2번쨰 표에 있는 값
# 해당 값에서 prod_name > a의 text를 추출
title = prod_items[1].select('p.prod_name > a')[0].text.strip()
print(title)

spec_list = prod_items[1].select('div.spec_list')[0].text.strip()
print(spec_list)

# replace를 사용해서 쉼표를 공백으로 변경
price = prod_items[0].select('li.rank_one > p.price_sect > a > strong')[0].text.strip().replace(',','')
# print(price)

def get_prod_items(prod_items):
    prod_data = []
    for prod_item in prod_items:
        try:
            title = title = prod_item.select('p.prod_name > a')[0].text.strip()
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

prod_data = get_prod_items(prod_items)
for i in prod_data:
    print(i)

driver.quit()