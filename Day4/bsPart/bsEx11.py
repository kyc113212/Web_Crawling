from bs4 import BeautifulSoup
from urllib.request import urlopen

def holly_store(result):
    # pageNo=1을 pageNo=%d로 변경
    # %d라는 값은 뒤의 %문자에따라서 변경된 숫자가 들어갈 수 있다
    for page in range(1, 6):
        holly_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store='%page
        # print(holly_url)
        html = urlopen(holly_url)
        bsObj = BeautifulSoup(html,'html.parser')
        # print(bsObj)
        tag_tbody = bsObj.find('tbody')
        for store in tag_tbody.findAll('tr'):
            # print(store.findAll('td', {'class':'noline center_t'}))
            # #print(store)
            # td와 같이 표로 되어있는 것은 배열처럼 index로 접근 할 수 있다.
            # td와 같은 것으 행을 기준으로 각 열을 기준으로 값을 받아 올 수 있다.
            store_td = store.findAll('td')
            store_name = store_td[1].text
            store_sido = store_td[0].text
            store_address = store_td[3].text
            store_phone = store_td[5].text
            result.append([store_name, store_sido, store_address, store_phone])


result = []
holly_store(result)
for i in result:
    print(i)
