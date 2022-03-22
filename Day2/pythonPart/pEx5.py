
#set은 중괄호로 표현한다
sdata = {3,2,4,1,2,4,1,2,3}
print(sdata)

#합집합, 교집합, 차집합, 대칭차집합 사용가능 set을 이용하여
sdata2 = {1,2,3,4}
sdata3 = {3,4,5,6}

#합집합
print(set.union(sdata2,sdata3))
print(sdata2.union(sdata3))
print(sdata2 | sdata3)

print()
#교집합
print(sdata2.intersection(sdata3))
print(sdata2 & sdata3)

print()
#차집합
print(sdata2.difference(sdata3))
print(sdata2 - sdata3)

print()
#대칭차집합 (합집합 - 교집합)
print(sdata2.symmetric_difference(sdata3))
print(sdata2 ^ sdata3)

print()
#리스트나 튜플을 set으로 사용하는 방법
ldata = [10,20,30,40,10,20,30]
sdata4 = set(ldata)
print(sdata4)

#빈 중괄호는 dict type으로 인식하므로 set객체는 아래와 같이 만든다
#dict의 해당하는 key값은 set으로 사용한다(중복사용x), value는 모든 오브젝트를 사용할 수 있다.

print()
sdata5 = {}
print(type(sdata5))

#비어있는 것을 set객체로 만드는 방법
sdata6 = set()
print(type(sdata6))