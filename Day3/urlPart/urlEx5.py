from urllib.request import urlopen
import re

url = 'https://finance.naver.com/item/main.naver?code=066570'
html = urlopen(url)
html_content = str(html.read().decode('ms949'))
#print(html_content)

#물음표가 정확히 어떤의미인지 복습때 확인
stock_results = re.findall(r'(\<dl class=\"blind\"\>)([\s\S]+?)\</dl\>',html_content)

lg_stock = stock_results[0]
#실제 사용 데이타
lg_index = lg_stock[1]
# print(lg_index)

index_list = re.findall(r'(\<dd\>([\s\S]+?)\<\/dd\>)', lg_index)
for index in index_list:
    print(2, index[1])