#
# class Person():
#     def __init__(self,name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#     def print_info(self):
#         print(f'name:{self.name}, age:{self.age}, adderss:{self.address}')
#
# smith = Person('smith',10,'seoul')
# smith.print_info()


class InstanceC:
    #text_list = []
    def __init__(self):
        self.text_list = []
    def add(self, text):
        self.text_list.append(text)
    def print_list(self):
        print(self.text_list)

obj1 = InstanceC()
obj1.add('first')
obj1.print_list()

#아래와 같이 하는 경우 obj1의 값도 포함되어 있다.
#클래스는 init이 아닌 변수 선언시 전역변수처럼 쓰여지는 형태로 만들어졌다 (text_list가)
# def __init__(self):
#     self.text_list = []
# 위처럼 init에 해줘야지 각각의 static변수처럼 사용된다.
obj2 = InstanceC()
obj2.add('second')
obj2.print_list()
