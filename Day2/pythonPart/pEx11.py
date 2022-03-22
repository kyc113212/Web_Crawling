
#return은 반환과 함수 종류
#yield는 반환을 하지만 함수 종료는 하지않고 대기한다

def num_generator():
    yield 0
    yield 1
    yield 2

# num_gerator를 호출하고 0에서 대기 -> 0을 반환
# 다시 다음에 요청에 대기하고 있던 yield0에서 다음 라인인 yield1로 이동하고 반환 후 대기
# 이렇게 마지막으로 가서 갈일이 없으면 yield는 자동적으로 StopIteration을 호출하여 loop를 종료해준다
for i in num_generator():
    print(i)

# 처음 n값이 0이고 3보다 적을때까지는 계속 동작시킨다.
# yield 0이후 값을 반환하고 대기 (yield 라인에서 대기한다)
# 다음에 요청하라때 yield다음 줄을 요청하고 yield 1를 반환하고 다시 대기
def CustomRange2(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

print()
for i in CustomRange2(3):
    print(i)

def gEx(datas):
    for str in datas:
        yield str.upper()

foods = ['juice', 'bread', 'steak']
for data in gEx(foods):
    print(data)