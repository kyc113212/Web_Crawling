import numpy as np

arr1 = np.arange(10)
print(arr1)
print(np.sqrt(arr1))
print()
print(np.cos(arr1))

arr2 = np.array([[2,6,7,3],[7,5,1,3],[0,2,9,8]])
print(arr2)
print('sum:',arr2.sum())
print('mean',arr2.mean())
print('std',arr2.std())

# (3,4)일때 처음은 axis 0축, 둘째 4는 axis 1축이다.
# 따라서 2차원 기준으로 axis가 0이면 열에 따른 값 계산 1이면 행에 다른 값을 계산한다
print(arr2.mean(axis=0))
print(arr2.mean(axis=1))

# 행렬을 원하는 size로 변환
arr3 = np.arange(12)
print(arr3)
print()
print(arr3.reshape(4,3))


