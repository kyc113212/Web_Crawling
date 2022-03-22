# for i in range(5):
#     print(i)
#
# #__iter__함수
# iter = range(3).__iter__()
# print(iter)
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())

class CustomRange():
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

# next를 동작할수 있게 하는 주소값을 iter에서 return해주는 것이다
    def __next__(self):
        if self.current < self.end:
            rvalue = self.current
            self.current += 1
            return rvalue
        else:
            raise StopIteration

for i in CustomRange(1,5):
    print(i)

print()
ddata = {'name':'kim', 'age':30, 'address':'seoul'}
#dict_keys객체 내부의 리스트로 저장이된다(키값과 value값 모두)
for k in ddata.keys():
    print(k)
