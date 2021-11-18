import numpy as np
#Factorizacion LU, matrices cuadradas

n = 3
#inicializar matriz original en ceros
matriz=np.zeros([n,n])
#matriz U
u=np.zeros([n,n])
#matriz L
l=np.zeros([n,n])
print("introduce los elementos de la matriz")
for i in range (0,n):
    for j in range (0,n):
        matriz[i,j]=(input("Elemento a["+str(i+1)+","+str(j+1)+"]"))
        u[i,j]=matriz[i,j]
#Número de condición de la matriz A
x=np.linalg.cond(matriz)
#hacer ceros debajo de la diagonal principal
for k in range (0,n):
    for i in range (0,n) :
        if (k==i):
            l[k,i]=1
        if(k<i):
            #eliminación gaussiana
            factor=(matriz[i,k]/matriz[k,k])
            l[i,k]=factor
            for j in range (0,n):
                matriz[i,j]=matriz[i,j]-(factor*matriz[k,j])
                u[i,j]=matriz[i,j]

print("Resultado")
print("Matriz L")
print(l)
print("Matriz U")
print(u)
print("numero de condición matriz A")
print(x)

#Error hacia adelante
aux = np.copy(x)
resultadoExacto = np.array([[-61/49],
                           [-4/7],
                           [57/49]])
resta = np.subtract(resultadoExacto,aux)
errorAdelante = np.linalg.norm(resta)
print('Error hacia adelante: ' , errorAdelante)


