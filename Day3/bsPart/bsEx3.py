from bs4 import BeautifulSoup

html_str ='''
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
'''

bsObj = BeautifulSoup(html_str, 'html.parser')
ul_tag = bsObj.find('ul')
#print(ul_tag.text)
litag = ul_tag.find('li')
print(litag)

# findAll을 하면 값들이 list형태로 들어온 것을 볼 수 있다.
litags = ul_tag.findAll('li')
#print(litags)

for li in litags:
    print(li.text)
