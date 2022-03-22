infile = open('UN.txt','r')
ldata = [line.rstrip('\n').split(',') for line in infile]
country = input('Enter the name of a continent: ')
print(ldata)
for i,j,k,v in ldata:
    if country == j:
        print(i)