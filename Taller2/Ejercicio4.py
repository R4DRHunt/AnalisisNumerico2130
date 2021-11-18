#AX=B
#Metodo SOR
#precision 10**-5
#b=bi=pi
#Ai={1,...,80}
import math
import numpy as np


def relajacion(A,b,x,w,tol):
  n=len(x)
  #residual=np.linalg.norm(np.matmul(A, x) - b)
  #while residual>tol:
  for j in range(n):
      s=0
      for i in range(n):
        s=s+A[i][j]*x[i]
      x[j]=x[i]+w*(b[i]-s)/A[j][j]
    #residual = np.linalg.norm(np.matmul(A, x) - b)
    #print('Residual: {0:10.6g}'.format(residual))
  return x

A=np.ones((81,81))
b=np.ones(81)
x=np.ones(81)
tol=1e-5
#condiciones

for j in range(1,81):
  b[j]=math.pi
  for i in range(1,81):
    if(j==i and i>=1):A[i][j]=2#*i
    elif(j==i+2 and i>=1 and i<=78):A[i][j]=0.5#*i
    elif(j==i-2 and 1>=3):A[i][j]=0.5#*i
    elif(j==i+4 and i>=1 and i<=76):A[i][j]=0.25#*i
    elif(j==i-4 and i>=5 ):A[i][j]=0.25#*i
    else :A[i][j]=0
#for it in range(10):
x=relajacion(A,b,x,0.5,tol); print(x)