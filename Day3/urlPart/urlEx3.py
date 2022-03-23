import urllib.request
import re
from urllib.request import urlopen

url = 'https://www.google.com/googlebooks/uspto-patents-grants-text.html'
html = urlopen(url)
html_content = str(html.read().decode('utf-8'))
url_list = re.findall(r'(http)(.+)(zip)',html_content)
#print(url_list)
for url in url_list:
    # 조인함수는 리스트를 하나로 합치는 것이다
    full_url = ''.join(url)
    print(full_url)
    #.은 문자 하나를 나타내며 +는 하나 이상
    file_name = re.findall(r'(ipg)(.+)(zip)',full_url)
    print(file_name)
    if len(file_name) > 0:
        #file name을 추출하여 urlretrieve를 이용해서 다운로드한다
        file_name = ''.join(file_name[0])
        print(file_name)
        #urllib.request.urlretrieve(full_url,file_name)
    print('end download')