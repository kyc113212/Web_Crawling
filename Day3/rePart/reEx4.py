import re

# 닷은 문자하나를 뜻하고 이 닷은 어떠한 문자든 상관없다
# .+ 는 어떠한 문자 상관없이 한개 이상을 뜻한다
# 아래와 같은 경우에는 맨처음의 <b>와 맨 마지막의 </b>만 찾아서 하나의 문자열로 출력
fdata1 =re.findall(r'<b>.+</b>', '<b>blog</b>is a<b>website</b>containg a body')
print(fdata1)

# ?가 의미하는 의미는 가장 가까운 것을 찾는 것이다
# <b>찾고 다음 </b>나오는 것을 찾아라는 것을 사용할때 ?사용
# <b>와 </b>사이에 모든 내용이 있고 가장 가까운것을 나누어서 찾으므로 리스트에 나눠서 들어갈 수 있다.
fdata2 =re.findall(r'<b>.+?</b>', '<b>blog</b>is a<b>website</b>containg a body')
print(fdata2)