from urllib.request import urlopen
import json
from_data = '2010-01-01'
to_data = '2021-12-31'

url = 'http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/'+from_data+'/edate/'+to_data

text = urlopen(url)
json_obj = json.load(text)
pieces = []
for item in json_obj:
    print(f'date:{item["date"]}, price:{item["settlement"]}')
    pieces.append(float(item['settlement']))

import matplotlib.pyplot as plt
plt.plot(pieces)
plt.show()