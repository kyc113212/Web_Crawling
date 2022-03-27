from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service('../webcrawlingPart/chromedriver.exe')

def search_coffeBeanStore(result):
    cb_url = 'https://www.coffeebeankorea.com/store/store.asp'

    driver = webdriver.Chrome(service=s)

    for i in range(1,5):
        driver.get(cb_url)
        time.sleep(2)
        # 자바 스크립트의 함수를 불러온다
        try:
            # 자세히보기의 버튼 위에 커서를 올려놓으면 왼쪽 하단에 javascript 코드와 pop number가 표시된다.
            # 해당 값을 %d으로 정의하고 i로 넣는다.
            driver.execute_script('storePop2(%d)'%i)
            time.sleep(2)
            html = driver.page_source
            bsObj = BeautifulSoup(html,'html.parser')
            # div의 클래스명은 .으로 표현하고 그 아래에 있는 h2를 store name으로 가져온다
            # store_name_h2의 객체가 bs4의 resultset으로 찍히는데 이것의 텍스트를 가져오기위해서는 list형식의 0번째로 받은다음 text처리 해야한다.
            store_name_h2 = bsObj.select('div.store_txt > h2')
            # print(store_name_h2)
            # print(type(store_name_h2))
            store_name = store_name_h2[0].text
            print(store_name)
            # print(store_name_h2)
            # tbody로 되어있는 표형식을 가져오는 것은 실제로 가져올 태그인 td를 select하면 배열형식으로 가져온다.
            store_info = bsObj.select('div.store_txt > table.store_table > tbody > tr > td')
            #리스트로 나누면 실제 내용과 아래 주석이 나누어진다
            #리스트로 나눠진 내용의 필요한 값인 실제내용인 0번쨰 index값을 불러온다
            # 주소는 "서울시~" 다음에 span class가 있는데 이것은 리스트로 구분이 된다. 따라서 0번째 index의 값을 가져온다.
            store_address = list(store_info[2])[0]
            store_phone = store_info[3].text
            result.append([store_name, store_address, store_phone])
        except:
            continue
    driver.quit()

result = []
search_coffeBeanStore(result)
# print(result)
