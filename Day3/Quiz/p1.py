from urllib.request import urlopen
import re

# 정규식으로만 구현

url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
html = urlopen(url)
html_content = str(html.read().decode('utf-8'))
#print(html_content)

# url, title을 뽑아서 출력
#title_result = re.findall(r'\<a href=\"store\/books\/look+', html_content)
#title_result = re.findall(r'\<a href=\"/store/books/look\.+([\s\S]+?)\<\/a\>', html_content)
info_result = re.findall(r'\<a href=\"(/store/books/look\.php\?p_code=[\w]+)\"\>([\s\S]+?)\<\/a\>', html_content)
for info_list in info_result:
    str = 'http://www.hanbit.co.kr'+info_list[0]
    print("url:", str)
    print("title:", info_list[1])
    print('---')