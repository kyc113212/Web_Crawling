from bs4 import BeautifulSoup

html_str ='''
<html>
    <body>
        <ul class='greet'>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class='replay'>
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
'''

# ul에서 replay class를 가져오기 위해서는 아래와 같이 작업한다
# dict 방식으로 class와 class명을 가져오면 된다 
bsObj = BeautifulSoup(html_str, 'html.parser')
url_replay = bsObj.find('ul',{'class':'replay'})
print(url_replay)

for li in url_replay.findAll('li'):
    print(li.text)