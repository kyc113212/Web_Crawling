
a = (5,33,77)
b = (44,823,11)
c = (10,50,90)

list = [i+j+k for i,j,k in zip(a,b,c)]
print(list)