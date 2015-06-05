from scipy.integrate import odeint
from scipy import linalg
import numpy as np
class Lorenz(object):
    """Wil iemand me a.u.b.
    
    uitleggen waarom dit moet :(
    """
    def __init__(self,startpunt,sigma,rho,beta):
        self.startpunt=startpunt
        self.sigma=sigma
        self.rho=rho
        self.beta=beta
    def f(self,y,t):
        y=[y[0],y[1],y[2]]
        return [self.sigma*(y[1]-y[0]),y[0]*(self.rho-y[2])-y[1],y[0]*y[1]-self.beta*y[2]]
    def solve(self,T,dt):
        tijden=[]
        m=0
        while m<=T:
            tijden.append(m)
            m=m+dt
        return odeint(self.f,self.startpunt,tijden)
    def df(self,u):
        A=np.array([[-1*self.sigma,self.sigma,0],[self.rho-u[2],-1,-u[0]],[u[1],u[0],-self.beta]])
        return A
    def isStable(self,u):
        B=linalg.eigvals(self.df(u))
        return(B[0]<0 and B[1]<0 and B[2]<0)