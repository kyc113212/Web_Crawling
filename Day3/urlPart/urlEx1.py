from urllib.request import urlopen
#
# # urlopen은 홈페이지에 대한 정보를 보는 것
# uf = urlopen('http://www.daum.net')
# # 이것은 client 정보를 전달해준다.
# # server에 request하고 server가 준 response해주는데 이 response 객체를 보여준다.
# print(uf)
# print(uf.read())
# # 상태정보 404, 200등
# print('status:', uf.status)
# # 콘텐트 타입
# print('content-type:', uf.getheader('Content-Type'))


uf2 = urlopen('https://www.hanbit.co.kr/store/books/full_book_list.html')
# 아래와 같이 출력하면 깨져있는데, decoding이 제대로 되어있지 않아서 그렇다.
print(uf2)
# 해당 타입을 찾아보면 utf-8로 되어있다
# 못읽어 오는 경우 failobj='utf-8'를 이용하여 fail시 utf-8을 읽어오라 한다.
encoding = uf2.info().get_content_charset(failobj='utf-8')
print(encoding)

text = uf2.read().decode(encoding)
print(text)