
Pres = open("USPres.txt",'r')
Vice = open("VPres.txt",'r')

sdata1 = {p for p in Pres}
sdata2 = {v for v in Vice}

idata = sdata1.intersection(sdata2)
print(sdata1 & sdata2)

outfile1 = open('bdata.txt','w')
outfile1.writelines(idata)
outfile1.close()

ldata = sorted(idata)
print(ldata)

outfile2 = open('bdata2.txt','w')
outfile2.writelines(ldata)
outfile2.close()