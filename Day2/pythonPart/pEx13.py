# 파일 입출력

# infile = open('States.txt','r')
# rstr = infile.read()
# print(rstr)
# infile.close()

# infile1 = open('States.txt','r')
# for line in infile1:
#     print(line)

infile2 = open('States.txt','r')
ldata = [line for line in infile2]
print(ldata)
ldata.sort()
print(ldata)

outfile = open('StatesAlpha.txt','w')
outfile.writelines(ldata)
infile2.close()
outfile.close()