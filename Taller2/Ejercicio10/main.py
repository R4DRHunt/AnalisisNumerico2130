import numpy as np

def F(x):
    f1 = x[0]**2+x[1]**2-1
    f2 = -x[0]+x[1]
    return np.array([f1,f2])

def df(x):
    return np.array([[2*x[0],2*x[1]],
                    [1,-1]])

N=100
x=np.array([1,1])

for k in range(N):
    xold = x
    Jinv = np.linalg.inv(df(x))
    x = x-np.dot(Jinv,F(x))
    x=x-np.dot(Jinv,F(x))
    e=np.linalg.norm(x-xold)
    print(k,x,e)
