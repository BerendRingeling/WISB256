def findRoot(f,a,b,epsilon):
    m=(a+b)/2
    if abs(a-b)<=epsilon:
        return m
    elif f(m)*f(b)<=0:
        return findRoot(f,m,b,epsilon)
    else:
        return findRoot(f,a,m,epsilon)