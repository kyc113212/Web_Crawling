# ddata = {'name':'kim', 'age':30, 'address':'seoul'}
#
# #dict_keys객체 내부의 리스트로 저장이된다(키값과 value값 모두)
# print(ddata.keys())
# print(ddata.values())
#
# for k in ddata.keys():
#     print(k)
#
# print()
# for d in ddata.items():
#     print(d[0],d)
# for k,v in ddata.items():
#     print(k, v)

ddata = {'name':'kim', 'age':30, 'address':'seoul'}

def print_info(name,age,address):
    print(f'name:{name}, age:{age}, address:{address}')
print()

#*를 의미하는 것은 unpacking이다.
#언팩킹시
ldata = [10,20,30]
print(*ldata)
print()

#아래와 같이 **입력으로 나눠서 넣을필요가 없다
#(원래대로라면 ddata['name'], ddaata['age'] ~와 같이 넣는다)
# **은 딕셔너리를 가변인자처럼 변경해서 전달하는 것이다.
print_info(**ddata)
print()

#아래와 같은 경우는 data를 함수에서 가변인자로 받아오는 것이며, 이것을 함수는 dict으로 받아온다.
def print_info2(**data):
    for k,v in data.items():
        print(k,v,sep=":")

print_info2(name='kim',age=30,address='busan',weight=90)
print()

#quit함수 원형을 보면 아래와 같이 되어있는데 이는 인자를 10,20,age:30,name:"kim" 이렇게 전달할 수 있는 것이다.
#
# def quit(*args, **kwargs): # real signature unknown
#     pass