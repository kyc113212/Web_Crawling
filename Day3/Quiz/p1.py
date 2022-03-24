# from urllib.request import urlopen
# import re
#
# # 정규식으로만 구현
#
# url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
# html = urlopen(url)
# html_content = str(html.read().decode('utf-8'))
# #print(html_content)
#
# # url, title을 뽑아서 출력
# #title_result = re.findall(r'\<a href=\"store\/books\/look+', html_content)
# #title_result = re.findall(r'\<a href=\"/store/books/look\.+([\s\S]+?)\<\/a\>', html_content)
# info_result = re.findall(r'\<a href=\"(/store/books/look\.php\?p_code=[\w]+)\"\>([\s\S]+?)\<\/a\>', html_content)
#
# for info_list in info_result:
#     str = 'http://www.hanbit.co.kr'+info_list[0]
#     print("url:", str)
#     print("title:", info_list[1])
#     print('---')
#
#     #urlEx3참고
#     #urlEx5참고
# #
# # info_result2 = re.findall(r'(\<td class=\"left\"\>)([\s\S]+?)\</table\>',html_content)
# # info_result3 = re.findall(r'\<a([\s\S])+href=\"([\s\S]+?)',info_result2)
# # print(info_result3)


# lazy와 greedy
# // Greedy
# '010-1234-5678'.match(/-\d+/g); // ['-1234', '-5678']
#
# // Lazy
# '010-1234-5678'.match(/-\d+?/g); // ['-1','-5']
# 정규표현식에서 +는 {1,}과 같다. 즉 최소 한 개 이상 최대 무한 개 까지 매칭한다.
# Greedy이기 때문에 "최대한 많이" 매칭하기 때문에 ['-1234', '-5678']가 매칭되었다.
# 하지만 Lazy하게 동작하도록 뒤에 ?를 추가하면 (+?, {1,}?) 한 개만 매칭되어도 정규표현식을 만족하기 때문에 ['-1','-5']가 매칭된다.

##답
import re
from urllib.request import urlopen


f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')

# HTTP 헤더를 기반으로 인코딩 방식을 추출합니다(명시돼 있지 않을 경우 utf-8을 사용하게 합니다).
encoding = f.info().get_content_charset(failobj="utf-8")
# 인코딩 방식을 표준 오류에 출력합니다.
html = f.read().decode(encoding)

# 정규식의 greedy와 lazy형식에 대해서 복습때 공부
# re.findall()을 사용해 도서 하나에 해당하는 HTML을 추출합니다.
for partial_html in re.findall(r'<td class="left"><a.+?</td>', html):
    #print(partial_html)
    # 도서의 URL을 추출합니다.
    url = re.search(r'<a href="(.+?)">', partial_html).group(1)
    url = 'http://www.hanbit.co.kr' + url
    # 태그를 제거해서 도서의 제목을 추출합니다.
    # 내부에 있는 객체들 중 <>안에 잇는 모든 내용을 공백으로 변경한다.
    title = re.sub(r'<.+?>', '', partial_html)
    print('url:', url)
    print('title:', title)
    print('---')


