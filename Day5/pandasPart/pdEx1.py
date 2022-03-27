
#시리즈 객체는 index 중복 허용한다.

import pandas as pd
import numpy as np

#인덱스를 따로 지정해주지 않으면 자동으로 만들어 준다
obj1 = pd.Series([3,4,5,6])
print(obj1)

# 인덱스를 아래와 같이 넣을 수 있으며 중복된 index(a)를 넣을 수 있다.
obj2 = pd.Series([3,4,5,6], index=['a','c','a','d'])
print(obj2)
# print에도 해당하는 index를 모두 찾아서 반환한다.
print(obj2['a'])
print(obj2.values)

print(obj2['c'])
obj2['d'] = 2000
print()
print(obj2)
print()
print(obj2*3)
print()
print(np.exp(obj2)) #exp는 지수함수(e^x)를 의미한다.

obj2 = pd.Series([3,4,5,6], index=['a','c','a','d'])
print(obj2 > 4)
print(obj2[obj2 > 4])

print()
# dict를 key:value로 선언하고 이것을 시리즈 객체로 선언하면 자동으로 index - value관계로 시리즈에 저장된다.
ddata = {'one':300, 'two':500, 'three':700}
obj3 = pd.Series(ddata)
print(obj3)