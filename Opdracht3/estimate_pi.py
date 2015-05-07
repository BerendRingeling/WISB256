import random
import math
import sys


try:
    N=int(sys.argv[1])
except IndexError:
    print('Use: estimate_pi.py N L')
    sys.exit()
try:
    L=float(sys.argv[2])
except IndexError:
    print('Use: estimate_pi.py N L')
    sys.exit()
if L>1:
    print('AssertionError: L should be smaller than 1')
    sys.exit()
if len(sys.argv)==4:
    zaad=sys.argv[3]
    random.seed(zaad)
a=[0]*N
i=0
hits=0
while i<N:
    y=random.random()
    z=random.vonmisesvariate(0,0)
    p=y+L*math.cos(z)
    if p<0 or p>1:
        a[i]=True
        hits=hits+1
    i=i+1
print(hits,'hits in',N,'tries')
if hits==0:
    print('Pi =','100')
else:
    print('Pi =',L*(2/(hits/N)))


