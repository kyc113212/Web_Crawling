# # 1. 공공데이터포털 사이트의 국립중앙의료원 전국 약국 정보 조회 서비스 데이터를 이용하여 코드를 진행하시오
# #
# #
# #
# #   ㄱ. 서울특별시에 있는 약국 데이터만 사용한다
# #
# #   ㄴ. 파라미터 일부는 다음과 같다
# #
# #        ORD='NAME',  pageNo='1', numOfRows='5000'
# #
# #   ㄷ. 가져온 데이터에서 월요일 오후9시 초과까지 운영하는 약국의 수를 출력하시오
# 
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import quote_plus
# 
# # endpoint는 여기서 약국정보에 대한 key이다
# # 뒤에 쿼리가 들어와야 하므로 endpoint뒤에 Queste mark - ? 가 꼭 들어와야한다
# endpoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
# # servicekey는 내가 인증받은 키이다. data.go.kr에 내 계정에만 있는 하나의 키
# serviceKey = 'xLROZfflVtihGq4aJ7zgU5BhIb554bNgu8MZjDf8BiuwnB2YkW6H2quB8c9WO2sDH9KanoRwtyxt8KRPoj3OVQ%3D%3D'
# 
# Q0 = quote_plus('서울특별시')
# ORD = 'NAME'
# pageNo = '1'
# numOfRows = '5000'
# parameter = 'serviceKey=' +serviceKey+'&Q0='+Q0+'&ORD='+ORD+'&pageNo='+pageNo+'&numOfRows='+numOfRows
# url = endpoint + parameter
# result = requests.get(url)
# bsObj = BeautifulSoup(result.content,'lxml')
# #dutytime할때 모두 소문자로 해야한다
# cnt = 0
# for i in bsObj.findAll('item'):
#     #if(((int)i.text) > 2100)
#     #dutytime1c
#     #print(i)
#     try:
#         if int(i.find('dutytime1c').text) > 2100:
#             print(i.find('dutyname').text)
#             cnt+=1
#     except AttributeError as err:
#         print("약국명 없음")
#         print(err)
# print(f'21시 이상 영업하는 약국의 수 : {cnt}')


##강사 정답
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup

seoul = '서울특별시'

endpoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = 'jcIDt4PJUiyQbVi14kCIL5rsq5i80l605%2FQ3TgBUlOp8I3qqrQt472uuqTPSIBL2CDvpA09wHbpr6hs3%2BCrOjg%3D%3D'
Q0 = quote('서울특별시')
ORD = 'NAME'
pageNo = '1'
numberOfRows = '5000'
pageSize = '10'

paramset = "serviceKey="+serviceKey+"&Q0="+Q0+"&ORD="+ORD+"&pageNo="+pageNo+"&numOfRows="+numberOfRows+"&pageSize="+pageSize

url = endpoint + paramset
print(url)

result = requests.get(url)

bs_obj = BeautifulSoup(result.content, 'lxml')
items = bs_obj.findAll('item')

count = 0
for item in items:
    tag_item = item.find('dutytime1c')
    if(tag_item != None):
        close_time = int(tag_item.text)
        if(close_time > 2100):
            count +=1
print('월요일 9시 이후까지 하는 약국의 수:'+ str(count))

