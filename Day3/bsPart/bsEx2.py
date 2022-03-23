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

# 객체에서 div인것을 모두 찾아서 list형대로 넣고, for문에서 각 list의 항목에서 text항목만 뺴서 출력
for list in bsObj.findAll('div'):
    print(list.text)