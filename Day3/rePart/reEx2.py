import re

#그룹 개념

robj1 = re.match(r'[a-zA-Z0-9]+', 'Hello1234')
print(robj1)

#소괄호는 그룹 개념이다, white space 기준으로 소괄호면 white space기준으로 나눠진다는 것이다
#정수 + white space + 정수 format을 찾으라는 것
robj2 = re.match(r'([0-9]+) ([0-9]+)', '322 777 good')
print(robj2)
robj4 = re.findall(r'([0-9]+)', '322 777 good')
#group의 0번째는 전체, 1은 첫번째 그룹, 2는 두번째 그룹을 나타낸다
print(robj2.group(0))
print(robj2.group(1))
print(robj2.group(2))
# 그룹을 멤버를 튜플형식으로 가져온다
print(robj2.groups())
print(robj4[0])

#정규식에 id를 부여하여 group을 이용해서 호출한다.
# (?P<func>[a-zA-Z_][a-zA-Z0-9_]+)는 그룹으로 묶은 후 ?P를 통해서 func이라고 명칭한다음에
# (?P<arg>\w+)는 그룹으로 붂고 ?P를 통해서 해당 그룹을 arg라고 명칭하고 모든 정수/문자에 대해서 그룹
print()
robj3 = re.match(r'(?P<func>[a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(42323)')
print(robj3)
print(robj3.groups())
print(robj3.group('func'))
print(robj3.group('arg'))