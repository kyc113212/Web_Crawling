import re

#정규식 표현을 통해 해당하는 문자열을 바꿔준다
#apple과 orange가 fruit으로 바꾼다
cstr1 = re.sub(r'apple|orange', 'fruit','apple box orange box')
print(cstr1)

cstr2 = re.sub(r'나의|내', '그의', '나의 물건에 손대지 마시오')
print(cstr2)

#바꾸려는 값에 함수를 넣어서 변경할 수도 있다.
def multi10(m):
    n = int(m.group())
    return str(n*10)

cstr3 = re.sub(r'[0-9]+', multi10, '23 function22 642 fruit 3')
print(cstr3)

# 역슬래시 2개는 그룹을 나타나게 해준다 //2 2번그룹, //1번그룹
print()
cstr4 = re.sub(r'([a-z]+) ([0-9]+)', '\\2 \\2 \\1', 'hello 2323')
print(cstr4)

# 키와 밸류가 있는 dict를 <name>kim</name>형식으로 변경
# \s는 whitespace, tab, new line을 통칭해서 쓸 수 있는 것이다.
print()
# 순서대로 설명하자면
# (는 그룹 지정
# /{는 표현식일수 있는 {를 포함
# /s*는  whitespace로 앞에 공백이 있을수도 있고 없을수도 있고
# )는 그룹을 닫고
# \"는 표현식일수있는 "을 포함
# (\w+)는 정수및 문자모두를 포함
# \"는 표현식일 수 있는 "을 포함
# \:는 표현식잀 수 있는 :를 포함
# \s*는 앞에 공백이 있을수도 없을수도
cstr5 = re.sub(r'(\{\s*)\"(\w+)\"\:\s*\"(\w+)\"(\s*\})', '<\\2>\\3</\\2>' ,'{ "name": "kim" }')
print(cstr5)