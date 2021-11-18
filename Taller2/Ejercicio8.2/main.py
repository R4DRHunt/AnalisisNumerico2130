import np as np
import numpy

x = [[1,-8,-2],[1,1,5],[3,-1,1]]
y = [1,4,-2]
def gauss(x,y):
    f = len(y)
    c = np.zeros([f,f+1])
    for i in range (f):
        for j in range (f):
            c[i][j] = x[i][j]
        c[i][f] = y[i]
    for k in range(f):
        t = c[k][k]
        for j in range (k,f+1):
            c[k][j] = c[k][j]/t
        for i in range(k+1,f):
            t = c[i][k]
            for j in range (k, f+1):
                c[i][j] = c[i][j]-t*c[k][j]
    h =np.zeros([f,1])
    h[f-1] = c[f-1][f]

    for i in range(f-2, -1, -1):
        s = 0
        for j in range(i+1,f):
            s += c[i][j]*h[j]
        h[i]=c[i][f]-s
    return h

h = gauss(x,y)
print (" -- Resultado --")
print(h)

def error_relativo(v_obtenido,v_real):
    rta = np.linalg.norm(v_obtenido-v_real)/np.linalg.norm(v_real)
    return rta
rta = error_relativo(h,x)
print("Error Relativo")
print(rta)

#Error hacia adelante
aux = np.copy(x)
resultadoExacto = np.array([[-61/49],
                           [-4/7],
                           [57/49]])
resta = np.subtract(resultadoExacto,aux)
errorAdelante = np.linalg.norm(resta)
print('Error hacia adelante: ' , errorAdelante)

#Error hacia atras
multiMatriz = np.matmul(x,aux)
resta2 = np.subtract(y,multiMatriz)
errorAtras = np.linalg.norm(resta2)
print("Error hacia atras: ", errorAtras)

def numeroDeCondicion(x):
    num_condicion_inf = np.linalg.cond(x,np.inf)
    print("----")
    print("Numero de condicion: ", num_condicion_inf)
    return num_condicion_inf
numeroCondicion1 = numeroDeCondicion(x)

