import pandas as pd
import numpy as np

frame1 = pd.DataFrame([[3,2,1],[5,6,7]])
print(frame1)

frame2 = pd.DataFrame([[3,2,1],[5,6,7]],index=['one','two'],columns=['first','second','third'])
print(frame2)

print()
ldata = [('kim',10,160),('lee',20,180),('oh',170,50)]
frame3 = pd.DataFrame(ldata,columns=['name','age','height'])
print(frame3)

# index는 행의 정보를 나타내고, column은 열의정보를 나타낸다.
# dict형식에서 key-value를 정하고 dataframe에 넣으면 column에 키가 지정된다.
print()
ddata = {'state':['seoul','busan', 'incheon'], 'pop':[1000, 5000, 300]}
frame4 = pd.DataFrame(ddata,index=['one','two','three'])
print(frame4)

# 행-열을 바꾸려면 transpose 사용
print()
print(frame4.transpose())

# 시리즈 객체로 가져온다
# 따라서 구조적인 문제로 state와 같이 column값은 가져올 수 있는데, two와 같은 행값은 따로 명시를 해줘야 가져올 수 있다. (loc 메서드를 사용)
print()
# iloc은 index 번호로 판단
print(frame4.iloc[1])
print()
print(frame4.state)
print()
print(frame4.loc['two'])