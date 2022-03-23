from bs4 import BeautifulSoup

html_str ='''
<html>
    <div>hello</div>
    <div>good day</div>
</html>
'''

bsObj = BeautifulSoup(html_str, 'html.parser')
#print(bsObj)

# find는 하나만 찾는다(처음 찾는 객체를 리턴)
print(bsObj.find('div'))
print(bsObj.find('div').text)

print(bsObj.findAll('div'))