from urllib.request import urlopen
import re

url = 'https://finance.naver.com/item/main.naver?code=066570'
html = urlopen(url)
html_content = str(html.read().decode('ms949'))
#print(html_content)

#물음표가 정확히 어떤의미인지 복습때 확인
#그룹 내에서 가장 가까운 것을 찾는다?
#동일한 형식을 나눈다.
stock_results = re.findall(r'(\<dl class=\"blind\"\>)([\s\S]+?)\</dl\>',html_content)
#print(stock_results)
lg_stock = stock_results[0]
#실제 사용 데이타
lg_index = lg_stock[1]
print(lg_index)

# 물음표는 앞에 내온 캐릭터가 선택사항(있어도 되고 없어도되는)임을 의미
# 그룹 안에 그룹? -> 반복되는 dd라는 태그 내에서 문자열을 추출
# 그룹 1은 dd태그까지 포함한 문자열이고, 그룹 2는 그안에있는 <dd>를 제외한 문자열이다
index_list = re.findall(r'(\<dd\>([\s\S]+?)\<\/dd\>)', lg_index)
for index in index_list:
    print(2, index[0], index[1])