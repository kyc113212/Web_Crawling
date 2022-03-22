# # 람다함수
#
# def f1(x):
#     return x ** 2
# print(f1(10))
#
# # 좌측이 매개변수, 우측이 return값
# f2 = lambda x:x**2
# print(f2(10))
#
# # 코드의 가독성을 높이기 위해 lambda를 사용한다
# def calc(cf,a,b):
#     result = cf(a,b)
#     print('result:', result)
#
# # 람다에서는 좌측이 매개변수, 우측이 return값
# calc(lambda x,y: x*y,100,200)
#
# # map을 이용하여 원하는 타입으로 정수를 받아서 변수에 저장
# value1, value2 = list(map(int, input("두 정수 값을 입력하세요:").split()))
# print(value1, value2)
# print()
#
# # map에 값을 전달할때 int에서 lambda로 변경해서 사용할 수 있다
# value3, value4 = list(map(lambda x:int(x)*100, input("두 정수 값을 입력하세요:").split()))
# print(value3, value4)
# print()

ldata = [4,2,9,1,7,5,6]
ldata.sort()
print(ldata)

#sort내부에도 lambda를 사용하여 dict에대해 필요한 인자를 sort해서 사용할 수 있다.
ldata2 = [('kim',88),('lee',90),('choi',78),('park',100)]
ldata2.sort(key=lambda x: x[1])
print(ldata2)