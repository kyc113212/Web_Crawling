from urllib.request import urlopen
import re

# group을 사용할 수 있는 것은 match메서드를 사용했을 때만 사용가능하다
# findall은 list객체러 전달해주기 때문에 group을 사용하지 않아도 index로 접근가능하다.

url = 'https://goo.gl/U7mSQl'
html = urlopen(url)
html_content = str(html.read().decode('utf-8'))

# 내가 한 방식
# print(html_content)
# id_list = re.findall(r'(\w+\*\*\*+)',html_content)
# for i,j in enumerate(id_list, start=1):
#     print(i,j)

# 강사 방식
result = re.findall(r'[a-zA-Z0-9]+\*\*\*',html_content)
for i,j in enumerate(result, start=1):
    print(i,j)
