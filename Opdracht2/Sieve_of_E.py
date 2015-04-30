import time
import sys


T1=time.perf_counter()
maxi=int(sys.argv[1]) #deze eerste 6 regels zijn bedoeld om [2,...,maxi] te construeren
a=[0]*maxi
i=2
while i<maxi:
    a[i] = i
    i=i+1

x=2 #deze zeven regels vormen de kern van het programma
while x<maxi:
    k=2
    while x*k<maxi:
        a[x*k]=0 #elk niet priem  element wordt nu naar nul afgebeeld
        k=k+1
    x=x+1


prm=open(sys.argv[2],"w")
s=2
while s<maxi:
    if a[s]>0:
        prm.write(str(a[s])+'\n')
    s=s+1

b=list(set(a))
b.remove(0)
b.sort()
T2=time.perf_counter()
print('Found', len(b),'Prime numbers smaller than',str(maxi),'in',T2-T1,'sec.')