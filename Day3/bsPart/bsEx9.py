from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

pages = set()

def getLinks(pageUrl):
    html = urlopen('https://en.wikipedia.org'+pageUrl)
    bsObj = BeautifulSoup(html,'html.parser')

    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').findAll('p'[0]))
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('이 페이지에는 해당 속성 값이 없습니다')

    # wiki를 정규식으로 만들기 위해 compile이라는 정규식 변경 method를 사용한다.
    # wiki로 시작하는 것을 추려낸다
    for link in bsObj.findAll('a', href=re.compile('^/wiki/')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 페이지를 계속 이동하면서 href라는 attribute를 찾은다음에
                # 처음방문한 page인 경우 계속 recursive하게 타고 들어가는 로직
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

#처음에는 본페이지부터 시작하게
getLinks('')