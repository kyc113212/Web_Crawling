from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html, 'html.parser')

for link in bsObj.find('div', {'id':'bodyContent'}).findAll('a'):
    # href라는 속성값이 link의 속성값(attrs)에 있는지 확인
    # 아래 print 내용을 확인해보면 #이 있는데 이 명령어는 내부이동이므로 이것은 제거해야한다.
    # 풀네임으로 http:~로 시작하는 것은 외부이동 사이트주소이다
    if 'href' in link.attrs:
        print(link.attrs['href'])
