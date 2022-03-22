
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

# 함수리스트를 만들수 있다
# 아래와 같이 index와 인자를 모두 넣어서 호출가능
flist = [add, subtract]
print(flist[0](10,20))
print(flist[1](10,20))

# 함수인자에도 함수를 넣을 수 있다.
# calc호출시 add함수를 전달한다.
def calc(cf, a, b):
    rvalue = cf(a,b)
    print(rvalue)

calc(add,30,70)
