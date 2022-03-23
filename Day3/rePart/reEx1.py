import re

#정규식 공부

# Hello를 정규식으로 만들기 위해 compile이라는 정규식 변경 method를 사용한다.
# 정규식은 컴파일이란 과정을 거치는데 search와 같은 것을 호출할때마다 자체적으로 compile하는 것은 성능상에 부담이 있기때문에 사용하기 좋게 미리 정규식으로 컴파일한다.
r1 = re.compile('Hello')
# r1이라는 정규식을 넣어주고 뒤에 문자열중에 r1의 정규식을 찾는 method이다
fobj1 = re.search(r1, 'good Hello World')
print(fobj1)
# 찾은 문자열 start,end 위치
print(fobj1.span())
# 찾은 문자열 내용
print(fobj1.group())
print(fobj1.group(0))

#앞에 r'Hello'처럼 r을 넣거나 찾을 문자열만 넣어도 serch사용 가능하다
print()
fobj2 = re.search(r'Hello', 'good Hello World')
print(fobj2)
fobj3 = re.search('Hello', 'good Hello World')
print(fobj3)

#search는 전체에서 찾는 것이고, match는 맨앞에서 있는지 찾는것이다
print()
fobj4 = re.match('Hello', 'Hello good Hello World')
print(fobj4)

# Hello가 두개있는데 search는 처음의 hello만 표시한다, 모두 찾기위해서는(index 포함x) findall을 사용해야한다(리스트 형식으로 반환)
print()
fobj5 = re.search('Hello', 'Hello good Hello World')
print(fobj5)
fobj6 = re.findall('Hello', 'Hello good Hello World')
print(fobj6)

# a는 1개이상 b는 0개이상의 문자를 찾는다.
print()
fobj7 = re.findall(r'a+b*', 'aaaa cc bbb aabb')
print(fobj7)

#맨 앞에 Hello가 있는지 확인
fobj8 = re.findall('^Hello', 'Hello good Hello World')
print(fobj8)

#앞에 0하고 9중에서 한개를 포함하는것
fobj9 = re.findall('[0-9]+', 'Hello good Hello 53 4 World')
print(fobj9)

# 중괄호를 이용해서 앞에글자의 2개이상 3개이하를 찾는 방법 (h가 2개이상 3개이하를 찾는다)
fobj10 = re.findall(r'h{2,3}', 'Hello ghhood Hello 53 4 ddddddddddhhhWorld')
print(fobj10)

# 0부터9까지 되는것이 2,3개 하이픈 들어가있고 0부터9까지 3개나 4개이후 하이픈하고 숫자 4개
# 0-9와 \d는 동일한 표현이다
fobj11 = re.findall(r'[\d]{2,3}-[0-9]{3,4}-[0-9]{4}', 'Hello tel:010-7878-8989 Hello 017-134-2212ghhood 02-232-1123Hello 53 4 ddddddddddhhhWorld')
print(fobj11)

# a-zA-Z는 문자열 모두 포함
fobj12 = re.findall(r'[a-zA-Z]+', 'good tel:010-8989-8989 hj Hello')
print(fobj12)

# \w+는 a-z, A-Z, 0-9 _까지 다 포함하는 것이다
fobj13 = re.findall(r'\w+', 'good tel:010-8989-8989 hj Hello')
print(fobj13)

# \W+(대문자)는 부정을 의미하며 정수, 알파벳 이외의 모든것(ex) _)까지 다 포함하는 것이다. 위의 문자 숫자를 제외한게 리스트로 전달받는다
fobj14 = re.findall(r'\W+', 'good tel:010-8989-8989 hj Hello')
print(fobj14)