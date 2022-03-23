import re

# 닷은 문자하나를 뜻하고 이 닷은 어떠한 문자든 상관없다
# .+ 는 어떠한 문자 상관없이 한개 이상을 뜻한다
fdata1 =re.findall(r'<b>.+</b>', '<b>blog</b>is a<b>website</b>containg a body')
print(fdata1)

# ?가 의미하는 의미는 가장 가까운 것을 찾는 것이다
# <b>찾고 다음 </b>나오는 것을 찾아라는 것을 사용할때 ?사용
fdata2 =re.findall(r'<b>.+?</b>', '<b>blog</b>is a<b>website</b>containg a body')
print(fdata2)