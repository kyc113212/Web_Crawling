from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.naver.com'
html = urlopen(url)
bsObj = BeautifulSoup(html,'html.parser')

start_page = bsObj.find('div',{'class':'service_area'})
print(type(start_page))
# print(start_page)
# start_page는 bs4의 element이므로 bs4메서드인 find, findall사용한다.
first_atag = start_page.find('a')
print(first_atag.text)
#찾은 tag에서부턴 dict형태로 되어있는듯 하다 dict형태는 어디서부터 접근해야하는지 확인필요
print(first_atag['href'])