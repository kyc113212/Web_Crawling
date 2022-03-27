import numpy as np
import pandas as pd

frame1 = pd.DataFrame(np.arange(8).reshape(2,4),
                      columns=['d','a','b','c'],
                      index=['three','one']
                      )

print(frame1)
print()
#row의 index값에 대한 indexing
print(frame1.sort_index(axis=0))
print()
print(frame1.sort_index(axis=1))
print()
# 오른차순 False로 decending으로 구현
print(frame1.sort_index(axis=1,ascending=False))

frame2 = pd.DataFrame({'b':[4,7,-3,2], 'a':[0,1,0,1]})
print(frame2)
print()
# sort를 value기준으로 하고 기준 colume을 정해준다.
print(frame2.sort_values(by='b'))

print()
# a,b 의 순서대로 sorting
print(frame2.sort_values(by=['a','b']))

print()
# a,b 의 순서대로 sorting
print(frame2.sort_values(by=['a','b'], ascending=[True,False]))
