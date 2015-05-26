import math
class Vector(object):
    """wtf moet hier staan????
    
    attributes: 'n','element'
    """
    def __init__(self,n,element=[0]):
        if isinstance(element,float):
            self.element=[element]*n
        elif isinstance(element,int):
            self.element=[element]*n
        elif isinstance(element,list):
            if element==[0]:
                self.element=n*[0]
            else:
                self.element=element
    def __str__(self):
        return '\n'.join([str(x) for x in self.element])
    def norm(self):
        return math.sqrt(self.inner(self))
    def lincomb(self,other,alpha,beta):
        w=[(alpha*float(self.element[i])+beta*float(other.element[i])) for i in range(len(self.element))]
        return Vector(len(w),w)
    def scalar(self,alpha):
        return self.lincomb(self,alpha,0)
    def inner(self,other):
        return sum(self.element[i]*other.element[i] for i in range(len(self.element)))
    def add(self,other):
        return self.lincomb(other,1,1)
    def __add__(self,other):
        return self.add(other)
    def substract(self,other):
        return self.lincomb(other,1,-1)
    def __sub__(self,other):
        return self.substract(other)
    def __mul__(self,alpha):
        return self.scalar(alpha)
    def proj(self,other):
        a=self.inner(other)/(self.norm()**2)
        return self*a
def GrammSchmidt(q):
    lijst=[0]*len(q)
    lijst[0]=q[0]*(1/q[0].norm())
    i=1
    while i<len(q):
        lijst[i]=q[i]-SumVector([lijst[j].proj(q[i]) for j in range(i)])
        lijst[i]=lijst[i]*(1/lijst[i].norm())
        i=i+1
    return lijst
def SumVector(L):
    s=[0]*len(L)
    s[0]=L[0]
    i=1
    while i<len(L):
        s[i]=s[i-1]+L[i]
        i=i+1
    return(s[len(L)-1])
