# infile = open('UN.txt','r')
# ldata = [line.rstrip('\n').split(',') for line in infile]
# country = input('Enter the name of a continent: ')
# print(ldata)
# for i,j,k,v in ldata:
#     if country == j:
#         print(i)

continent = input('Enter the name of a continent: ')
# 첫번째 글자를 대문자로, 이외의 글자는 소문자로 변경하는 것이 title
continent = continent.title()
infile = open('UN.txt', 'r')
for line in infile:
    data = line.split(',')
    if data[1] == continent:
        print(data[0])

infile.close()

