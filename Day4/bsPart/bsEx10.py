from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import string

def clearSentence(sentence):
    sentence = sentence.split(' ')
    # string.punctuation은 특수기호를 의미한다. 특수문자와 whitespace를 날린다
    sentence = [word.strip(string.punctuation+string.whitespace) for word in sentence]
    # 한글자 이상인 문자만 추출한다
    sentence = [word for word in sentence if len(word) > 1]
    return sentence

def clearInput(content):
    # 모두 대문자로
    content = content.upper()
    #print(content)
    # 제거해야할 것 제거 - 역슬래쉬와, 이 문장의 | 명령어로 or연산
    content = re.sub(r'\n|\[\d+\]', ' ', content)
    #print(content)
    content = bytes(content, 'utf-8')

    # ascii로 바뀌지 않는 특수기호는 무시한다
    content = content.decode('ascii','ignore')
    content = content.split('. ')
    # 컴프리 헨션을 이용하여 content에서 뽑아는 sentence를 cleaerSentence 함수에 넣어서 이용
    # [3]이 제거되고 \n이 제거된 상태에서 .으로 구분된 것
    return [clearSentence(sentence) for sentence in content]

from collections import Counter

def getNgramsFromSentence(content, n):
    output = []
    # n은 여기서 2로 왔으므로 len(content)는 리스트의 갯수 -n은 2개 + 1 -> 2개씩 묶는다
    # output에 i:i+n을 슬라이싱을 해줬으므로 2개씩 묶어진 것이 output에 들어간다.
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

def getNgrams(content, n):
    content = clearInput(content)
    ngrams = Counter()
    ngrams_list = []
    for sentence in content:
        # 리스트로 나누어져 있는 ngrams를
        newNgrams = [' '.join(ngrams) for ngrams in getNgramsFromSentence(sentence, n)]
        # append는 리스트를 이루어진게 있으면 리스트 자체를 넣고, extend는 항목이 리스트로 오면 그 리스트 내부의 항목의 요소를 분리하여 추가한다.
        ngrams_list.extend(newNgrams)
        # 추가된 newNgrams를 counting한다. 기존에 있던 것 + 1을해서 빈도수를 높인다
        ngrams.update(newNgrams)
    return ngrams, ngrams_list


#ngram 공부
#print(getNgrams('it is a good day!!!! python[3]. @have a good day', 2))

html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html,'html.parser')
# 본문에 들어간 데이터를 모두 출력
content = bsObj.find('div', {'id':'mw-content-text'}).getText()
# print(content)
ngrams, nlist = getNgrams(content,2)
print(ngrams)