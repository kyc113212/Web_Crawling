from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.naver.com'
html = urlopen(url)
bsObj = BeautifulSoup(html,'html.parser')

# ul태그에 있는 class이름이 list~인 것을 일단 page에 넣고 그 안에 tag가 a인것을 찾아 넣는다
list_page = bsObj.find('ul', {'class':'list_nav type_fix'})
list_atag = list_page.findAll('a')
for list in list_atag:
    print(list.text)