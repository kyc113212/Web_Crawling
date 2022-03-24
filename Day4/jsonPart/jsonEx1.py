# json파일을 읽어오기 위해서는 import json이 필요
import json

# json파일은 대체로 dict형식으로 되어있고 dict처럼 데이터를 추출하면 된다
file = open('json_example.json', 'r', encoding='utf-8')
content = file.read()
file.close()
jdata = json.loads(content)

print(jdata)
for data in jdata['employees']:
    print(data['firstName']+' : '+ data['lastName'])