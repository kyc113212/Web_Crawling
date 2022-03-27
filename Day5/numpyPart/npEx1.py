import numpy as np

data1 = [6,7,8,1.5,2]
print(data1)
print(type(data1))
print()

arr1 = np.array(data1)
# dtype으로 int형으로 바꿀수 있다
arr1 = np.array(data1, dtype=np.int32)
print(arr1)
print(type(arr1))
print()

data2 = [[1,2,3],[4,5,6]]
print(data2)
print()

arr2 = np.array(data2)
print(arr2)
print(arr2.shape)
print()

arr3 = np.arange(1,10)
print(arr3)
print()

# start와 end사이를 균등하게 자른 샘플을 표시
arr4 = np.linspace(-3,3,50)
print(arr4)
print()

arr5 = np.ones([3,4])
print(arr5)
print()

arr6 = np.zeros([3,4])
print(arr6)
print()

# 최근에 할당된 것 중에서 자기와 똑같은 크기를 가지고 있는 배열을 재할당
# 아래는 위가 zeros로 할당되어 있기 때문에 0으로 받고 바로 앞에 ones가 있으면 1로 받는다
arr7 = np.empty([3,4])
print(arr7)
print()