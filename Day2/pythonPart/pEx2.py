str1 = 'it is a good day'

# 아무것도 input하지 않으면 공백을 return해준다.
data = str1.split('i')
print(data)
data2 = str1.split(' ')
print(data2)

# split뒤에 나타나는 숫자는 n개만 자르고 그 뒤는 놔두는 것
# 자르는 갯수로 생각하자
print(str1.split(' ',1))
print(str1.split(' ',2))
print(str1.split(' ',3))
