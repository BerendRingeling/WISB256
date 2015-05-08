import math
import sys

count=0
for line in open(sys.argv[1]):
    count=count+1

a=[]
for line in open(sys.argv[1]):
    a=a+[int(line)]

z=[0]*count
j=0
count2=0
while j<count-1:
    if a[j+1]-a[j]==2:
        z[j]=a[j]
        count2=count2+1
    j=j+1
    
p=list((set(z)))
p.remove(0)
p.sort()
M=int(line)/(math.log(int(line)))
C=0.6601618


print('Largest Prime =',int(line))
print('--------------------------------')
print('pi(N)         =',count)
print('N/Log(N)      =',M)
print('ratio         =',(1/M)*count)
print('--------------------------------')
print('pi_2(N)       =',count2)
print('2CN/log(N)^2  =',2*C*int(line)/(math.log(int(line))**2))
print('ratio         =',count2*(1/(2*C*int(line)/(math.log(int(line))**2))))