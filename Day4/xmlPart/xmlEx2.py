# data.go.kr에서 원하는 data를 가져온다
# 예를 들어 국립중앙의료원을 검색해서 Api를 사용해야하고 이를 위해선 활용신청을 한다.
# pip install requests 설치 필요

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


# endpoint는 여기서 약국정보에 대한 key이다
# 뒤에 쿼리가 들어와야 하므로 endpoint뒤에 Queste mark - ? 가 꼭 들어와야한다
endpoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
# servicekey는 내가 인증받은 키이다. data.go.kr에 내 계정에만 있는 하나의 키
serviceKey = 'xLROZfflVtihGq4aJ7zgU5BhIb554bNgu8MZjDf8BiuwnB2YkW6H2quB8c9WO2sDH9KanoRwtyxt8KRPoj3OVQ%3D%3D'

# quote에 대한 공부가 필요
# 서울특별시를 utf-8으로 바꿔준 값을 Q0로 집어넣는다
# 이후에 쭉 관련된 값을 모두 수집한 다음에 쿼리를 포함하여 전달한다
Q0 = quote_plus('서울특별시')
#print(Q0)
Q1 = quote_plus('강남')
QN = quote_plus('삼성약국')
QT = '4'
ORD = 'NAME'
pageNo = '1'
numOfRows = '10'
# parameter가 여러개 있는경우는 &로 구분을 해준다.
parameter = 'serviceKey=' +serviceKey+'&Q0='+Q0+'&Q1='+Q1+'&QN='+QN+'&pageNo='+pageNo+'&numOfRows='+numOfRows
#parameter = 'serviceKey=' +serviceKey+'&Q0='+Q0
#아래 url은 서울,강남에 있는 삼성약국이 포함된 약국을 표시해준다
url = endpoint+parameter
# xml형식으로 넘겨준것
print(url)

#약국이름을 가져와햐한다
#url에서 get방식(post도있음)으로 가져온 값은 BeautifulSoup에 사용할때 content라는 method로 보내주어야한다.
result = requests.get(url)
bsObj = BeautifulSoup(result.content,'lxml')
items = bsObj.findAll('item')
for item in bsObj.findAll('dutyname'):
    print(item.text)