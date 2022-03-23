import re
from bs4 import BeautifulSoup

html_str='''
<html>
    <body>
        <ul class='ok'>
            <li>
                <a href='http://www.daum.net'>다음</a>
            </li>
            <li>
                <a href='http://www.naver.com'>네이버</a>
            </li>
        </ul>
        <ul class='fsite'>
            <li>
                <a href='http://www.google.com'>구글</a>
            </li>
            <li>
                <a href='http://www.facebook.com'>페이스북</a>
            </li>
        </ul>
    </body>
</html>
'''

# bsObj = BeautifulSoup(html_str, 'html.parser')
# atag = bsObj.find('a')
# print(atag)
# #위는 딕셔너리방법으로 값을 가져오므로 링크만 가져오기 위해서는 아래와 같이 가져와야한다.
# print(atag['href'])

bsObj = BeautifulSoup(html_str, 'html.parser')
atags = bsObj.findAll('a')
# #print(atags)
# for tags in atags:
#     print(tags)
link_list = []
title_list = []

#dict형식으로 되어있기 때문에 'herf'라는 키로 주소를 불러올 수 있다.
#title은 태그 안에 있는 text이므로 text메서드 추가해서 가져올 수 있다.
for link in atags:
    link_list.append(link['href'])
    title_list.append(link.text)
print(link_list)
print(title_list)