# comprehension (컴프리헨션)

data1 =[i for i in range(10)]

print(data1)
print()

#조건문이 하나인 경우 if문을 뒤에다 놓고, 조건문이 if - else인 경우 리스트에 input될 값(들) 뒤에 if/else문을 구현한다.
data2 = [i for i in range(10) if i %2==0]
print(data2)
print()

# 홀수인 경우 100의 값을 집어 넣는다.
# else가 있는경우 조건문을 컴프리헨션 앞쪽에 넣는다
data3 = [i if i % 2 == 0 else 100 for i in range(10)]
print(data3)
print()

# for문 앞에 리스트형식으로 만들어서 해당 값을 가공하는것도 가능.
str1 = "have a good day"
data4 = [[w.lower(), w.upper(), len(w)] for w in str1.split()]
print(data4)
print()

# enumberate는 리스트 값을 추출할 때 인덱스와 값을 언패킹하는 것이다
# start 속성은 index의 값을 start부터 시작하게 해주는 것
data = ['tic','tak','tok']
for i,v in enumerate(data, start=3):
    print(i,v)
print()

#dict를 이용한 comprehension함수
#enumerate는 index와 value를 빼주는 것이므로 i:j는 index와 value의 관계인 상태에서 dict으로 저장되는 것이다
str2 = 'it is a good day'
data5= {i:j for i, j in enumerate(str2.split())}
print(data5)
print()

#병렬형태로 묶기위해서는 zip을 사용하면 된다
ldata1 = ['kim','lee','oh']
ldata2 = ['seoul','busan','ulsan']

for d in zip(ldata1, ldata2):
    print(d)
print()

data6 = {i : d for i, d in enumerate(zip(ldata1,ldata2))}
print(data6)