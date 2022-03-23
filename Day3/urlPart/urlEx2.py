import re
from urllib.request import urlopen

uf = urlopen('https://www.hanbit.co.kr/store/books/full_book_list.html')
byte_content = uf.read()

# 못읽어오는 경우 replace option을 사용하여 �로 표히하게한다
# 전체 문자열 중에 charset="utf-8"을 찾아봐야한다.
scanned_text = byte_content[0:1024].decode('ascii', errors='replace')
#print(scanned_text)

# fdata = re.findall(r'\"utf-8\"', scanned_text)
# print(fdata)
# 아래와 같이 그룹으로 묶어야 mobj에서 그룹으로 판단하여 출력할 수 있다 소괄호()그룹 꼭 기억하자
# 뒤에 숫자 8은 그룹으로 묶는거전에 \"로 그룹 닫은 후에 "표시를 해주었으므로 -다음에 8까지 그룹에 포함된다
mobj = re.search(r'charset=\"([\w-]+)\"',scanned_text)
print(mobj.group())
print(mobj.group(1))

if mobj:
    encoding = mobj.group(1)
else:
    encoding = 'utf-8'
text = byte_content.decode(encoding)
print(text)