import pandas as pd
import numpy as np
#
# df1 = pd.read_csv('ex1.csv')
# print(df1)
# print()
#
# # header를 none으로 하면 colume에대한  index를 자동으로 생성해준다.
# df2 = pd.read_csv('ex2.csv', header=None)
# print(df2)
# print()
#
# # colum의 name을 정의해주는 것은 names 메서드를 사용한다.
# df3 = pd.read_csv('ex2.csv', names=['one','two','three','four','info'])
# print(df3)
# print()
#
# # 하나의 열을 index로 지정해줄 수 있다, index_col을 이용하여
# # 행의 이름을 정해주는 것은 아래 데이터가 수십 수만개가 있을 수 있기때문에 어렵고 하나의 열을 index로 지정하는건 가능
# df4 = pd.read_csv('ex2.csv',
#                   names=['one','two','three','four','info'],
#                   index_col='info')
# print(df4)
# print()
#
# #index_col의 순서로도 write할 수 있다.
# df5 = pd.read_csv('ex2.csv',
#                   names=['one','two','three','four','info'],
#                   index_col=1)
# print(df5)
# print()
#
# # 0번과 2번, 3번의 row를 제외
# df6 = pd.read_csv('ex4.csv', skiprows=[0,2,3])
# print(df6)
# print()
#
# frame = pd.DataFrame([[10,20,30],[100,200,300]],
#                      columns=['first', 'second', 'third'])
# print(frame)
# # index(row의 명칭)파트를 없애주기 위해 index=False 옵션을 준다
# frame.to_csv('sdata.csv')
# frame.to_csv('sdata2.csv', index=False)

frame2 = pd.DataFrame(np.random.randn(1000,3),
                      columns=['first','second','third'])
print(frame2)
print()
print(frame2.info)
print(frame2.head(10))
print()
print(frame2.tail(10))
print()
print(frame2.describe())